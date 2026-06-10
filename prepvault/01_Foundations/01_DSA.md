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
| **Two Pointers** | Deduplicating sorted logs, finding target pairs | Arrays, Strings | $O(N)$ Time, $O(1)$ Space |
| **Sliding Window** | Rate-limiting windows, streaming metrics | Arrays, Strings, Hash Maps | $O(N)$ Time, $O(K)$ Space |
| **Prefix Sums** | Database range query optimizations | Arrays | $O(1)$ query after $O(N)$ pre-process |
| **Fast & Slow Pointers** | Cycle detection in distributed state graphs | Linked Lists, Graphs | $O(N)$ Time, $O(1)$ Space |
| **Backtracking** | Parsing nested configurations, dependency trees | Recursion, Stacks | $O(2^N)$ or $O(N!)$ |
| **BFS & DFS** | Garbage collection tracing, network routing | Queues, Stacks, Graphs | $O(V + E)$ Time & Space |
| **Monotonic Stack/Queue** | Finding the next warm server in a cluster timeline | Arrays, Stacks, Queues | $O(N)$ Time, $O(N)$ Space |
| **Binary Search Variations**| Logarithmic search in segmented log files | Sorted Arrays | $O(\log N)$ Time, $O(1)$ Space |
| **Top-Down & Bottom-Up DP**| Resource allocation, knapsack container scheduling | Memoization tables, Arrays | $O(N \cdot W)$ Time |
| **Tries** | Autocomplete, IP routing, Prefix matching | Trees | $O(L)$ Time |
| **Heaps / Priority Queue** | Task scheduling, finding Top-K elements | Binary Heaps | $O(N \log K)$ Time |
| **Intervals** | Calendar booking, meeting room scheduling | Arrays | $O(N \log N)$ Time |

## Interview Think-Aloud Formula
During a live coding round, talk out loud:
- _“First, I’ll analyze the bounds to check for overflow...”_
- _“A naive nested loop gives $O(N^2)$, but using a sliding window with a hash map brings us to linear time $O(N)$ with $O(K)$ space...”_

## Related Topics
- [[01_Foundations/01_DSA/Arrays & Hashing/Index|Arrays & Hashing Index]]
- [[01_Foundations/01_DSA/Two Pointers/Index|Two Pointers Index]]
- (Other indexes...)
