---
type: concept
tags: [foundations, dsa]
created: 2026-06-10
---

# Data Structures & Algorithms (DSA): Patterns Over Memorization

> [!important] The 2026-27 Shift
> Master the underlying patterns to solve problems you've never seen before. In 2026, coding rounds test adaptation, not memory.

## The 12 Core Patterns Matrix

| Pattern | Real-World Application | Core Data Structures | Complexity Target |
| :--- | :--- | :--- | :--- |
| **[[01_Foundations/01_DSA/Two Pointers/Index|Two Pointers]]** | Deduplicating sorted logs, finding target pairs | Arrays, Strings | $O(N)$ Time, $O(1)$ Space |
| **[[01_Foundations/01_DSA/Sliding Window/Index|Sliding Window]]** | Rate-limiting windows, streaming metrics | Arrays, Strings, Hash Maps | $O(N)$ Time, $O(K)$ Space |
| **[[01_Foundations/01_DSA/Arrays & Hashing/Index#Prefix Sum|Prefix Sums]]** | Database range query optimizations | Arrays | $O(1)$ query after $O(N)$ pre-process |
| **[[01_Foundations/01_DSA/Linked Lists/Index#Two Pointers (Fast & Slow)|Fast & Slow Pointers]]** | Cycle detection in distributed state graphs | Linked Lists, Graphs | $O(N)$ Time, $O(1)$ Space |
| **[[01_Foundations/01_DSA/Backtracking/Index|Backtracking]]** | Parsing nested configurations, dependency trees | Recursion, Stacks | $O(2^N)$ or $O(N!)$ |
| **[[01_Foundations/01_DSA/Graphs/Index|BFS & DFS]]** | Garbage collection tracing, network routing | Queues, Stacks, Graphs | $O(V + E)$ Time & Space |
| **[[01_Foundations/01_DSA/Stack/Index#Monotonic Stack|Monotonic Stack/Queue]]** | Finding the next warm server in a cluster timeline | Arrays, Stacks, Queues | $O(N)$ Time, $O(N)$ Space |
| **[[01_Foundations/01_DSA/Binary Search/Index|Binary Search Variations]]**| Logarithmic search in segmented log files | Sorted Arrays | $O(\log N)$ Time, $O(1)$ Space |
| **[[01_Foundations/01_DSA/Dynamic Programming/Index|Top-Down & Bottom-Up DP]]**| Resource allocation, knapsack container scheduling | Memoization tables, Arrays | $O(N \cdot W)$ Time |
| **[[01_Foundations/01_DSA/Tries/Index|Tries]]** | Autocomplete, IP routing, Prefix matching | Trees | $O(L)$ Time |
| **[[01_Foundations/01_DSA/Heap & Priority Queue/Index|Heaps / Priority Queue]]** | Task scheduling, finding Top-K elements | Binary Heaps | $O(N \log K)$ Time |
| **[[01_Foundations/01_DSA/Intervals/Index|Intervals]]** | Calendar booking, meeting room scheduling | Arrays | $O(N \log N)$ Time |

## Interview Think-Aloud Formula
During a live coding round, talk out loud:
- _“First, I’ll analyze the bounds to check for overflow...”_
- _“A naive nested loop gives $O(N^2)$, but using a sliding window with a hash map brings us to linear time $O(N)$ with $O(K)$ space...”_

## Role-Specific Applications
- **[[02_Role_Tracks/02_Frontend_Engineer|Frontend]]**: DOM manipulation (Trees), state management (Arrays/Objects), virtualized lists (Sliding Window), undo/redo (Stack).
- **[[02_Role_Tracks/03_Backend_Engineer|Backend]]**: Database indexing (B-Trees), caching (LRU — Doubly Linked List + Hash Map), routing (Tries/Graphs), rate limiting (Sliding Window).
- **[[02_Role_Tracks/04_ML_Engineer|ML / Data Science]]**: NumPy/Tensor operations (Arrays), feature engineering, graph neural networks, decision trees.
- **[[02_Role_Tracks/05_DevOps_Engineer|DevOps]]**: Log parsing (Regex/Tries), network topology (Graphs), resource scheduling (Heaps), rate limiting (Token Bucket).
- **[[02_Role_Tracks/06_Data_Engineer|Data Engineering]]**: Data processing pipelines, shuffling algorithms, distributed sorting, hash-based partitioning.
- **[[02_Role_Tracks/07_Product_Manager|Product Management]]**: Understanding algorithmic constraints for product decisions, A/B testing statistical methods, time/space tradeoffs.

## Related Topics
- [[01_Foundations/02_SDLC|SDLC]]
- [[01_Foundations/03_System_Design|System Design]]
- [[01_Foundations/05_Networking|Networking]]
- [[02_Role_Tracks/01_General_SWE|General SWE Track]]
