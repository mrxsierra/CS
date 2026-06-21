---
type: concept
tags: [stack, backend, nodejs, javascript, v8, async]
created: 2026-06-10
---

# Backend Stack: Node.js Deep Dive

Node.js is a runtime environment that allows you to execute JavaScript on the server. For interviews, you must understand its non-blocking I/O model and the Event Loop.

---

## 1. The Architecture: V8 & Libuv
- **V8 Engine**: Developed by Google for Chrome. It compiles JavaScript directly to native machine code.
- **Libuv**: A multi-platform C library that provides support for asynchronous I/O based on event loops. It handles the thread pool, file system I/O, and network sockets.

## 2. The Event Loop (The Heart of Node)
Node.js is single-threaded for JavaScript execution but offloads I/O tasks to the system kernel or Libuv's thread pool.

### Phases of the Event Loop:
1. **Timers**: Executes callbacks scheduled by `setTimeout()` and `setInterval()`.
2. **Pending Callbacks**: Executes I/O callbacks deferred to the next loop iteration.
3. **Idle, Prepare**: Used only internally.
4. **Poll**: Retrieves new I/O events; executes I/O related callbacks.
5. **Check**: Executes `setImmediate()` callbacks.
6. **Close Callbacks**: Executes callbacks for closed events (e.g., `socket.on('close')`).

**Note on `process.nextTick()`**: It is NOT part of the event loop. It runs immediately after the current operation completes, regardless of the current phase.

## 3. Asynchronous Patterns
- **Callbacks**: The original pattern (leads to "Callback Hell").
- **Promises**: Objects representing the eventual completion (or failure) of an async operation.
- **Async/Await**: Syntactic sugar over Promises, making async code look synchronous.

## 4. Node.js Streams
Essential for handling large data (e.g., video streaming, large log files) without consuming too much memory.
- **Readable**: `fs.createReadStream()`
- **Writable**: `fs.createWriteStream()`
- **Duplex**: TCP sockets.
- **Transform**: `zlib` for compression.

## 5. Memory Management & Garbage Collection
Node.js uses the V8 garbage collector. 
- **Heap vs. Stack**: Primitive types go to the stack; objects/closures go to the heap.
- **Memory Leaks**: Often caused by global variables, uncleared timers, or forgotten closures.

## Common Interview Questions
- **"Is Node.js truly single-threaded?"**: JavaScript execution is single-threaded, but underlying I/O operations and Libuv work are multi-threaded.
- **"Explain the difference between `setImmediate()` and `setTimeout(fn, 0)`"**: `setImmediate` is designed to execute a script once the current poll phase completes. `setTimeout` schedules a script to be run after a minimum threshold.
- **"What is the 'Cluster' module?"**: A way to take advantage of multi-core systems by spawning a tree of Node.js processes.

## Related Topics
- [[01_Foundations/04_Operating_Systems|OS (Processes vs Threads)]]
- [[08_Stack_Deep_Dives/05_Databases_Stack/Index|Database Stack]]
