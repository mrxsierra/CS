---
type: concept
tags: [foundations, language-internals, go, goroutines, concurrency]
created: 2026-06-10
---

# Go Internals: GMP Scheduler, Memory Management, and Channels

Go is designed for modern, highly concurrent systems programming. It compiles directly to native machine code and embeds a lightweight runtime directly inside the application binary. This guide deep-dives into Go's runtime internals: the **GMP Scheduler**, **Memory and Stack management**, **Garbage Collection (GC)**, and the **Channel** architecture.

---

## 1. The G-M-P Scheduling Model

In traditional runtimes (like Java before Virtual Threads, or C++), concurrency is mapped directly $1:1$ to operating system (OS) kernel threads. This model is expensive: OS threads require a fixed stack space (~1MB) and context switches require entering kernel space, costing thousands of CPU cycles.

Go solves this via an **M:N Scheduler** managed entirely in user-space, which maps $M$ green-thread goroutines onto $N$ physical OS threads. The engine of this scheduler is the **GMP Model**:

```
                  +-----------------------+
                  |  Global Run Queue     | (Shared fallback queue, locked)
                  +-----------------------+
                              ^
                              | (Every 61 ticks, or when LRQ is empty)
                              v
+------------------+     +------------------+
|  Processor (P)   |     |  Processor (P)   | (Logical context, GOMAXPROCS)
|  Local Run Q (256|     |  Local Run Q (256| (Lock-free run queue)
|  [G1] [G2] [G3]  |     |  [G4] [G5] [G6]  |
+------------------+     +------------------+
         |                        |
         v                        v
+------------------+     +------------------+
|  M (OS Thread)   |     |  M (OS Thread)   | (Physical executor)
+------------------+     +------------------+
         |                        |
         v                        v
     Executing                Executing
     Goroutine (G)            Goroutine (G)
```

### 1.1 The G, M, and P Abstractions
*   **G (Goroutine)**: Represents a lightweight user-space thread. It contains:
    *   An execution stack (starts at 2KB, dynamically sized).
    *   An instruction pointer (PC) and CPU registers saved during context switches.
    *   Internal states: `_Gidle`, `_Grunnable`, `_Grunning`, `_Gsyscall`, `_Gwaiting`.
*   **M (Machine / OS Thread)**: Represents a physical operating system thread created and managed by the OS kernel. It is the actual executor of CPU instructions. 
    *   To run Go code, an `M` must acquire a logical processor `P`.
*   **P (Processor / Logical Context)**: Represents the resources required to execute Go code.
    *   The number of `P` instances is capped at the environment variable `GOMAXPROCS` (usually defaults to the machine's physical CPU core count).
    *   Each `P` maintains its own **Local Run Queue** (LRQ) of runnable goroutines, capped at 256 items. This local queue is lock-free (using CAS), making scheduling fast.

### 1.2 Run Queues & Starvation Prevention
*   **Local Run Queue (LRQ)**: Lock-free, per-P queue. If G1 spawns G2, G2 is placed on the active P's LRQ.
*   **Global Run Queue (GRQ)**: A shared, locked fallback queue. Goroutines go here if a P's LRQ overflows (exceeds 256), or if they are preempted after running too long.
*   **The 61-Tick Rule**: To prevent goroutines in the GRQ from starving, the scheduling loop checks the global queue exactly once every 61 scheduler ticks, bypassing the local queue.

### 1.3 Work Stealing Algorithm
When an OS thread `M` is running on context `P` and runs out of work (its Local Run Queue is empty), it attempts to find work using a strict priority order:
1.  Check the Global Run Queue (checked $1/61$ of the time).
2.  Check the Local Run Queue of `P`.
3.  Check the Network Poller (to see if any I/O bound goroutines are ready).
4.  **Work Stealing**: If still empty, `M` randomly selects another Processor `P'` and attempts to steal half of its runnable goroutines. This balances execution load across all CPU cores.

### 1.4 How Go Handles Blocking Operations

The GMP scheduler handles blocking operations differently depending on whether they are Network I/O or System Calls (Syscalls).

#### Network I/O (Integrated Network Poller)
When a Goroutine `G` blocks on a network read/write:
1.  `G` is detached from its current `M` and `P`, and its state changes to `_Gwaiting`.
2.  `G` is registered with the runtime's internal **Network Poller** (which wraps high-performance OS-level async polling like Linux `epoll`, macOS `kqueue`, or Windows `IOCP`).
3.  The physical thread `M` does not block. It immediately pulls the next runnable `G` from `P`'s queue and continues executing.
4.  When the OS notifies the Network Poller that the network socket is ready, the poller moves `G` back to a `P`'s local run queue or the GRQ, changing its state to `_Grunnable`.

#### System Calls (Blocking Syscalls)
When a Goroutine `G` invokes a blocking operation that cannot be polled (e.g., file system access or executing an external command):
1.  The executing thread `M` is forced to block inside the kernel.
2.  **Syscall Handoff**: The Go runtime detects that `M` is blocked in a syscall. It immediately detaches the logical Processor `P` from `M` (unmounting it).
3.  The runtime acquires or spawns a *new* physical OS thread `M'` and binds it to `P`. This allows other runnable goroutines on `P` to continue executing, preventing a single disk write from blocking the entire program.
4.  When the blocking system call eventually completes, the original `M` wakes up. It attempts to re-acquire an available logical `P` to resume running `G`. If no `P` is free, it puts `G` into the Global Run Queue and puts itself (`M`) to sleep in the thread pool.

### 1.5 Preemption: Cooperative vs. Asynchronous
*   **Cooperative Preemption (Go < 1.14)**: The compiler inserted stack-check instructions (`morestack()`) at the entry of every function. If a goroutine ran for more than 10ms, the runtime set a flag. When the goroutine next called a function, the stack check intercepted it and yielded execution. 
    *   *Flaw*: A tight mathematical loop (e.g., `for i := 0; i < 1e9; i++ { ... }`) containing no function calls could completely lock a thread, starving other goroutines.
*   **Asynchronous Preemption (Go 1.14+)**: The runtime uses OS-level signals. A background monitor thread (`sysmon`) runs periodically. If a goroutine is detected running continuously for more than 10ms on an `M`, `sysmon` sends an OS signal (**`SIGURG`** on Unix-like systems) directly to the target thread. The OS thread intercepts the signal, saves its execution context, and forces the running goroutine to yield, resuming it later.

---

## 2. Memory Allocation & Stack Internals

Go is a compiled systems language with automatic memory management. It achieves high speed by keeping allocations on the thread stack whenever possible.

### 2.1 Stack Allocation & Dynamic Growth
Unlike languages that allocate a fixed stack size per thread (like Java or C++), Go uses dynamically growing stacks:
*   **Initial Stack**: Each goroutine is initialized with a tiny 2KB stack.
*   **Segmented Stacks (Deprecated)**: In early Go versions, if a stack ran out of space, the runtime allocated a new "segment" of memory and linked it to the old stack using a pointer. 
    *   *Flaw*: The **Hot Split** problem. If a recursive function or loop repeatedly crossed the boundary of a segment, the runtime was forced to repeatedly allocate and deallocate stack segments, causing severe performance drops.
*   **Contiguous Stack Copying (Modern)**: If a goroutine exceeds its stack size, the runtime allocates a new contiguous memory block that is **double** the size of the original stack. It copies all existing stack frames into the new space and corrects all memory pointers to point to the new addresses. The old stack memory is released.

### 2.2 Escape Analysis
At compile time, Go executes a static analysis called **Escape Analysis** to determine if a variable's lifetime escapes the scope of the function that created it.
*   **Stack Allocation**: If the compiler proves a variable does not escape the function, it allocates it on the goroutine's stack. Stack allocation is incredibly fast (taking $O(1)$ CPU time by simply adjusting the stack pointer) and requires no garbage collection overhead.
*   **Heap Allocation**: If a variable escapes, it is moved to the global Heap. Heap allocation is slower and puts pressure on the Garbage Collector.

#### Common Escape Triggers
1.  **Returning pointers**: Returning a pointer to a local variable.
    ```go
    func getPointer() *int {
        x := 42
        return &x // x escapes to the heap because its pointer survives past function return
    }
    ```
2.  **Sending pointers to channels**: The compiler cannot predict which goroutine will read the data from a channel, so the underlying data must live on the heap.
3.  **Interface polymorphism**: Assigning variables to parameters of type `interface{}` (or `any` in Go 1.18+). Since interface execution uses dynamic dispatch, the compiler allocates the variable on the heap to preserve its memory layout.
4.  **Dynamic sizing**: Slices or maps whose size is determined by runtime variables rather than static compile-time constants.

---

## 3. The Go Garbage Collector

Go utilizes a **Concurrent, Tri-color Mark-and-Sweep** garbage collector. Unlike Java's standard collectors, Go's GC is **non-generational** and **non-compacting** (non-moving).

### 3.1 Why Go does not use a Generational or Compacting GC
1.  **Escape Analysis eliminates young-gen need**: In languages like Java, 95%+ of objects are short-lived, motivating a Generational GC. In Go, escape analysis already keeps short-lived variables on the thread stacks, where they are instantly freed without GC. The objects on the Go heap are mostly long-lived, reducing the benefit of young-gen segmentation.
2.  **Pointer pinning costs**: Compacting GCs move objects in memory to reduce fragmentation. Because Go allows direct pointer arithmetic and references in code, updating all references to a moved object in a highly concurrent systems environment introduces major performance bottlenecks.

### 3.2 The Tri-color Marking Algorithm
The collector categorizes all heap objects into three virtual colors:

```
[ White Objects ] <----- [ Grey Objects ] <----- [ Black Objects ]
(Unvisited, candidates)   (Visited, but children  (Visited, children
                          not yet scanned)        also scanned)
```

1.  **White**: Unvisited objects. At the start of GC, all objects are colored White. At the end, any objects remaining White are unreachable and will be swept (deleted).
2.  **Grey**: Objects that have been visited, but whose child references have not yet been scanned.
3.  **Black**: Objects that have been visited, and all of their child references have been scanned and colored Grey.

#### The GC Lifecycle Phases:
1.  **Sweep Termination (Stop-the-World - STW)**: Prepares the runtime for GC. Brings all running Ms to a halt.
2.  **Concurrent Marking**: 
    *   The GC colors all "GC Roots" (globals, variables on stacks, registers) Grey.
    *   Application threads resume running. GC worker threads concurrently pull objects from the Grey queue, scan their fields, color their children Grey, and color the parent Black.
3.  **Mark Termination (STW)**: A second tiny STW phase to finalize the marking of remaining grey items, turn off write barriers, and calculate the next GC trigger threshold.
4.  **Concurrent Sweep**: Reclaims memory. Loops through all White objects and returns their memory blocks to the free list, running concurrently with the live program.

### 3.3 The Write Barrier
Because application code runs concurrently during the "Concurrent Marking" phase, a thread could alter references behind the GC's back:
*   *The Hazard*: An application thread could write a reference from a Black object to a White object, and remove all references from Grey objects to that White object. Since a Black object's fields are already fully scanned, the GC will never visit the White object, mistakenly collecting it while it is still actively used!

To prevent this, Go uses a **Write Barrier** (specifically, a hybrid write barrier based on Dijkstra and Yuasa barriers):
*   During the marking phase, whenever an application thread attempts to overwrite a pointer in the heap, the write barrier intercepts the operation and colors the target object (or the new reference) **Grey** before performing the write. This preserves the "Tri-color Invariant" (ensuring no Black object can point directly to a White object without a Grey intermediate), ensuring safety during concurrent execution.

---

## 4. Channel Internals

Channels are Go's primitive for safe concurrent communication, implementing the mantra: *"Do not communicate by sharing memory; instead, share memory by communicating."*

A channel is *not* a lock-free structure. Under the hood, a channel is a concrete C-style struct called **`hchan`**, protected by a standard mutex.

### 4.1 Anatomy of the `hchan` Struct
The complete representation of a channel is defined in `/src/runtime/chan.go`:

```go
type hchan struct {
    qcount   uint           // Total data items currently in the queue buffer
    dataqsiz uint           // Size of the circular queue buffer
    buf      unsafe.Pointer // Pointer to an array representing the circular queue buffer
    elemsize uint16
    closed   uint32         // 0 if open, 1 if closed
    elemtype *_type         // Element type
    sendx    uint           // Send index in the circular buffer
    recvx    uint           // Receive index in the circular buffer
    recvq    waitq          // Linked list of waiting receivers (sudog nodes)
    sendq    waitq          // Linked list of waiting senders (sudog nodes)
    lock     mutex          // Mutex protecting all fields in hchan
}
```

```
+-------------------------------------------------------------------------+
|                                 hchan                                   |
|  [lock] Mutex                                                           |
|                                                                         |
|  [buf] Pointer to Circular Array  ---> [ [Data 1] [Data 2] [Empty] ]    |
|  [qcount] 2   [dataqsiz] 3                                              |
|  [sendx]  2   [recvx]    0                                              |
|                                                                         |
|  [sendq] Senders Queue (sudog)    ---> [ [G_sender_1] -> [G_sender_2] ] |
|  [recvq] Receivers Queue (sudog)  ---> [ [G_receiver_1] ]               |
+-------------------------------------------------------------------------+
```

*   **Circular Buffer**: `buf` is a pointer to a block of memory acting as a circular queue, managed by the read/write index pointers `recvx` and `sendx`.
*   **Wait Queues (`recvq` / `sendq`)**: Doubly-linked lists of waiting goroutines. A waiting goroutine is wrapped in an internal structure called a **`sudog`**, which stores the goroutine's `G` metadata, stack pointers, and a pointer to the memory location where the sent/received value should be copied.

### 4.2 Send / Receive Logic Deep Dive

#### Case 1: Unbuffered Channel Send
When a goroutine `G1` executes `ch <- value` on an unbuffered channel:
1.  `G1` acquires the channel's `lock`.
2.  **Fast Path (Direct Copy)**: If the receiver wait queue `recvq` is not empty (meaning `G2` is already blocked waiting for data):
    *   GC takes the `sudog` of `G2` from `recvq`.
    *   **Optimization**: The runtime copies the data directly from `G1`'s stack memory onto `G2`'s stack memory, bypassing the channel buffer entirely! This avoids heap allocation and memory copy overhead.
    *   `G2`'s state is changed to `_Grunnable` and it is sent to the scheduler.
    *   The channel lock is released.
3.  **Blocking Path**: If `recvq` is empty:
    *   The runtime allocates a `sudog` on `G1`'s stack.
    *   It packages `G1` and the address of `value` inside the `sudog`.
    *   The `sudog` is appended to the channel's `sendq`.
    *   The runtime calls **`gopark()`** to put `G1` to sleep (transitioning it to `_Gwaiting`).
    *   The channel lock is released. `G1` is now parked, and its thread `M` moves on to execute other goroutines.

#### Case 2: Buffered Channel Send
When a goroutine `G1` executes `ch <- value` on a buffered channel:
1.  `G1` acquires the channel's `lock`.
2.  If the circular buffer `buf` is not full (determined by comparing `qcount < dataqsiz`):
    *   The value is copied into `buf` at the slot indicated by `sendx`.
    *   `sendx` is incremented. If it reaches `dataqsiz`, it wraps around to $0$.
    *   `qcount` is incremented.
    *   The lock is released, and `G1` continues execution immediately without blocking.
3.  If the buffer is full:
    *   `G1` wraps itself in a `sudog` and appends it to `sendq`.
    *   The runtime calls `gopark()` to park `G1` and releases the channel lock.

#### Case 3: Closing a Channel
When `close(ch)` is called:
1.  Acquire the `lock`.
2.  Set `closed = 1`.
3.  Loop through `recvq`. Unpark all waiting receivers, returning the zero-value of the channel type and a boolean flag of `false` (e.g., `val, ok := <-ch` where `ok == false`).
4.  Loop through `sendq`. Unpark all waiting senders. **All waiting senders immediately panic!**
5.  Release the `lock`.

---

## 5. Complexity & Under-the-Hood Performance

### 5.1 Time & Space Complexity of Go Primitives

| Operation | Time Complexity | Space Complexity | Under-the-Hood Mechanism |
| :--- | :--- | :--- | :--- |
| **Goroutine Spawn** | $O(1)$ | 2KB | Allocates G and stack, pushes to Local Run Queue |
| **Goroutine Context Switch** | $O(1)$ (~10-100ns) | $O(1)$ | User-space register swap (no OS kernel transition) |
| **Channel Send/Recv (Uncontended)** | $O(1)$ | $O(1)$ | Mutex acquisition, direct stack copy or buffer write |
| **Channel Send/Recv (Contended)** | $O(1)$ (but blocks) | $O(1)$ | Goroutine parking (`gopark`), context switch |
| **Map Access / Write** | $O(1)$ (avg) | $O(1)$ | `hmap` bucket array, hashing, overflow bucket traversal |
| **Map Growth (Rehash)** | $O(N)$ (amortized) | $O(N)$ | Incremental rehashing (allocates double-sized bucket array, copies chunks of buckets on subsequent writes to avoid latency spikes) |

---

## 6. Common Interview Questions

### Q1: What is the G-M-P model in the Go scheduler, and why does Go need a logical Processor (P) instead of just mapping Goroutines (G) directly to OS Threads (M)?
**Answer:**
The logical Processor `P` is a critical optimization introduced in Go 1.1 to prevent thread contention.
In early versions of Go, the scheduler mapped `G` directly to `M`. All physical threads competed for a single, global, mutex-protected run queue. As multicore processor counts grew, threads spent more time waiting on the global scheduler mutex than executing code.

By introducing `P` as a logical context, Go partitioned the queues:
1.  **Thread Local Queues**: Each `P` owns its own local run queue (LRQ) of size 256. Running threads `M` only interact with their bound `P`'s LRQ, which is lock-free (using CAS), removing global lock contention.
2.  **Syscall Separation**: When a goroutine performs a blocking system call, the physical thread `M` blocks in the kernel. Without `P`, all other goroutines assigned to that thread would also block. Because Go has a separate `P` context, the runtime can detach `P` from the blocked `M` and migrate it to a new thread `M'`. This keeps the other goroutines on `P` running on a separate CPU core, while the old thread `M` safely blocks in the kernel.

### Q2: Walk through what happens internally when a Goroutine writes to a full channel.
**Answer:**
1.  The sending goroutine `G` acquires the internal mutex lock (`hchan.lock`) of the channel.
2.  The runtime checks if the channel is closed. If closed, the write fails and throws a panic.
3.  The runtime checks if there are any waiting receivers in the `recvq` queue. Since the channel buffer is full, there are none.
4.  The runtime checks if there is space in the circular buffer `hchan.buf`. Since the channel is full, `qcount == dataqsiz`, meaning there is no space.
5.  **Parking sequence**:
    *   The runtime allocates a synchronization node called a `sudog` on the stack of `G`.
    *   It sets `sudog.elem` to point to the memory location of the variable being sent.
    *   It appends the `sudog` to the `hchan.sendq` queue.
    *   It calls **`gopark()`**, instructing the Go scheduler to transition `G`'s state from `_Grunning` to `_Gwaiting` and detach it from its thread `M`.
    *   Crucially, **`gopark()` releases `hchan.lock`** immediately after detaching, allowing other threads to access the channel.
6.  The physical thread `M` is now free. It runs the scheduler loop, pulls the next runnable goroutine from its Processor `P`'s queue, and executes it.

### Q3: Why are Go maps not thread-safe? What happens if you try to concurrently read and write to a map, and how does the runtime detect this?
**Answer:**
Go maps are optimized for single-threaded performance. Adding lock-free mechanics or internal synchronization to all map operations would introduce heavy performance overhead (like atomic memory barriers or allocations), slowing down the majority of programs that do not share maps across threads.

If you attempt to concurrently write to a map while another thread is reading or writing to it, the application will experience a race condition, leading to memory corruption or undefined behavior. 

**Detection Mechanism**:
Go maps use a special bit flag to protect themselves at runtime. The internal map struct, `hmap`, contains a `flags` field:
*   Whenever a write or delete operation begins on a map, the runtime sets a write flag bit: `hmap.flags |= hashWriting`.
*   Whenever a read or write operation is invoked, the runtime immediately inspects this bit: `if hmap.flags & hashWriting != 0 { throw("concurrent map writes") }`.
*   If the flag is set during a read, it means a concurrent write is occurring. The runtime immediately throws a non-recoverable runtime crash: **`fatal error: concurrent map read and map write`**. This crash cannot be caught using `recover()`.

**Alternatives**:
1.  Wrap the standard `map` in a structure with a `sync.RWMutex`.
2.  Use **`sync.Map`**, which is optimized for disjoint keys, or write-once, read-many access patterns.

### Q4: Explain Go's Escape Analysis and name three distinct code patterns that trigger heap allocation.
**Answer:**
Escape Analysis is a static compiler analysis executed during compilation. It parses the Abstract Syntax Tree (AST) to trace the flow of variables. If a variable's reference remains accessible after its declaring stack frame is popped off the CPU stack, the variable is marked as "escaped" and is allocated on the Heap.

**Triggers**:
1.  **Returning a pointer to a local variable**:
    ```go
    func makeUser() *User {
        u := User{Name: "Alice"}
        return &u // Escapes! u must survive past the function call stack frame
    }
    ```
2.  **Using pointers with Interface types**:
    ```go
    func main() {
        x := 100
        fmt.Println(x) // Escapes! fmt.Println takes parameter of type "any/interface{}"
    }
    ```
    Under the hood, `any` wraps the primitive. Because interface execution uses dynamic dispatch and reflection at runtime, the compiler cannot guarantee the lifetime of `x` on the stack, forcing it to escape to the heap.
3.  **Slices with dynamic or oversized capacity**:
    ```go
    s := make([]int, size) // Escapes if "size" is a variable, or if size is constant but > 64KB
    ```

### Q5: What is the Stop-The-World (STW) penalty in Go, and how does the Go GC achieve sub-millisecond pauses compared to Java's collectors?
**Answer:**
The **Stop-The-World (STW)** penalty refers to the time during which the Go runtime halts all application goroutines. This is done to ensure the consistency of memory metadata (such as switching the write barriers on/off or finalizing GC roots) without race conditions from active threads.

Go achieves sub-millisecond STW pauses through several key architectural choices:
1.  **Concurrent Sweep & Mark**: The vast majority of GC work (99%) occurs concurrently while application goroutines are running. Go worker threads mark and sweep memory side-by-side with user code.
2.  **The Write Barrier**: Rather than pausing all threads to ensure marking correctness, Go uses a concurrent write barrier. This barrier intercepts pointer changes during active execution, ensuring no newly created references are missed during concurrent marking.
3.  **Non-compacting Design**: Java's GCs (like G1) achieve low fragmentation by compacting (moving) objects. Moving objects requires updating all reference pointers, a highly expensive operation that requires long STW pauses. Go's GC is non-moving; it keeps objects in place and uses a highly optimized thread-local free-list allocator (`mspan`) to handle fragmentation, trading off minor memory fragmentation for ultra-low latency.

---

## 7. [Role: Application]

### Backend Engineer
*   **Preventing Goroutine Leaks**: Always design your concurrent operations with a strict lifecycle. Unbounded goroutines that block forever on channels that are never read from will cause memory leaks. Use `context.WithTimeout` or `context.WithCancel` to guarantee termination.
*   **High Performance API Pooling**: When executing high-throughput JSON marshalling or database operations, utilize **`sync.Pool`** to cache and reuse temporary heap structures (like byte buffers or object models), reducing GC allocations.

### DevOps / SRE
*   **Tuning the GC with `GOGC`**: The `GOGC` environment variable determines how aggressively GC runs. The default is $100$ (GC runs when the heap doubles in size). Setting `GOGC=200` delays GC, saving CPU cycles at the cost of higher memory usage.
*   **Preventing Out-of-Memory with `GOMEMLIMIT`**: Introduced in Go 1.19, `GOMEMLIMIT` sets a hard memory cap (e.g., `GOMEMLIMIT=2GiB`). The runtime will dynamically increase GC frequency to enforce this limit before allowing the OS to kill the container via OOM-killer.

### Cloud Native / Systems
*   **Optimizing Docker Containers**: Because the Go runtime spawns physical threads based on `GOMAXPROCS` (which defaults to the host machine's total CPU count), running a Go container inside a Kubernetes pod with CPU limits (e.g., `limits: cpu: 2`) on a 64-core host can lead to severe performance degradation. Use the **`uber-go/automaxprocs`** library to automatically scale `GOMAXPROCS` to match the Pod's actual container limits.

---

## Related Topics
- [[01_Foundations/04_Operating_Systems|OS (Virtual Memory, Context Switches)]]
- [[01_Foundations/07_Language_Internals/Java|Java (JVM) Internals]]
- [[08_Stack_Deep_Dives/04_DevOps_Cloud/01_Docker|Docker Container Internals]]

## External Resources
- [The Go Runtime Source Code](https://github.com/golang/go/tree/master/src/runtime) - Open-source Go runtime.
- *Go Systems Programming* by Mihalis Tsoukalos - Excellent book on Go internals.
- [Ardan Labs: Go Scheduler Part 1 & Part 2](https://www.ardanlabs.com/blog/2018/08/scheduling-in-go-part1.html) - Celebrated deep dive on Go scheduling mechanics.
