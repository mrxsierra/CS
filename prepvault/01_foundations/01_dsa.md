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
| **[[01_foundations/01_dsa/two_pointers/index|Two Pointers]]** | Deduplicating sorted logs, finding target pairs | Arrays, Strings | $O(N)$ Time, $O(1)$ Space |
| **[[01_foundations/01_dsa/sliding_window/index|Sliding Window]]** | Rate-limiting windows, streaming metrics | Arrays, Strings, Hash Maps | $O(N)$ Time, $O(K)$ Space |
| **[[01_foundations/01_dsa/arrays_and_hashing/index#Prefix Sum|Prefix Sums]]** | Database range query optimizations | Arrays | $O(1)$ query after $O(N)$ pre-process |
| **[[01_foundations/01_dsa/linked_lists/index#Two Pointers (Fast & Slow)|Fast & Slow Pointers]]** | Cycle detection in distributed state graphs | Linked Lists, Graphs | $O(N)$ Time, $O(1)$ Space |
| **[[01_foundations/01_dsa/backtracking/index|Backtracking]]** | Parsing nested configurations, dependency trees | Recursion, Stacks | $O(2^N)$ or $O(N!)$ |
| **[[01_foundations/01_dsa/graphs/index|BFS & DFS]]** | Garbage collection tracing, network routing | Queues, Stacks, Graphs | $O(V + E)$ Time & Space |
| **[[01_foundations/01_dsa/stack/index#Monotonic Stack|Monotonic Stack/Queue]]** | Finding the next warm server in a cluster timeline | Arrays, Stacks, Queues | $O(N)$ Time, $O(N)$ Space |
| **[[01_foundations/01_dsa/binary_search/index|Binary Search Variations]]**| Logarithmic search in segmented log files | Sorted Arrays | $O(\log N)$ Time, $O(1)$ Space |
| **[[01_foundations/01_dsa/dynamic_programming/index|Top-Down & Bottom-Up DP]]**| Resource allocation, knapsack container scheduling | Memoization tables, Arrays | $O(N \cdot W)$ Time |
| **[[01_foundations/01_dsa/tries/index|Tries]]** | Autocomplete, IP routing, Prefix matching | Trees | $O(L)$ Time |
| **[[01_foundations/01_dsa/heap_and_priority_queue/index|Heaps / Priority Queue]]** | Task scheduling, finding Top-K elements | Binary Heaps | $O(N \log K)$ Time |
| **[[01_foundations/01_dsa/intervals/index|Intervals]]** | Calendar booking, meeting room scheduling | Arrays | $O(N \log N)$ Time |

## Interview Think-Aloud Formula
During a live coding round, talk out loud:
- _“First, I’ll analyze the bounds to check for overflow...”_
- _“A naive nested loop gives $O(N^2)$, but using a sliding window with a hash map brings us to linear time $O(N)$ with $O(K)$ space...”_

## Role-Specific Applications
- **[[02_role_tracks/02_frontend_engineer|Frontend]]**: DOM manipulation (Trees), state management (Arrays/Objects), virtualized lists (Sliding Window), undo/redo (Stack).
- **[[02_role_tracks/03_backend_engineer|Backend]]**: Database indexing (B-Trees), caching (LRU — Doubly Linked List + Hash Map), routing (Tries/Graphs), rate limiting (Sliding Window).
- **[[02_role_tracks/04_ml_engineer|ML / Data Science]]**: NumPy/Tensor operations (Arrays), feature engineering, graph neural networks, decision trees.
- **[[02_role_tracks/05_devops_engineer|DevOps]]**: Log parsing (Regex/Tries), network topology (Graphs), resource scheduling (Heaps), rate limiting (Token Bucket).
- **[[02_role_tracks/06_data_engineer|Data Engineering]]**: Data processing pipelines, shuffling algorithms, distributed sorting, hash-based partitioning.
- **[[02_role_tracks/07_product_manager|Product Management]]**: Understanding algorithmic constraints for product decisions, A/B testing statistical methods, time/space tradeoffs.

## Related Topics
- [[01_foundations/02_sdlc|SDLC]]
- [[01_foundations/03_system_design|System Design]]
- [[01_foundations/05_networking|Networking]]
- [[02_role_tracks/01_general_swe|General SWE Track]]
