---
type: concept
tags: [foundations, dsa, heap-priority-queue]
created: 2024-06-10
---

# Heap & Priority Queue

## Overview
A Heap is a specialized tree-based data structure that satisfies the heap property. A Priority Queue is an abstract data type implemented using a Heap.

## Key Principles & Patterns
- Min-Heap / Max-Heap: The root is always the smallest or largest element.
- Complete Binary Tree: Heaps are usually implemented using arrays for efficiency.
- Heapify: The process of creating a heap from an array in O(n) time.

## Complexity Analysis
| Operation | Complexity |
|-----------|------------|
| Push/Insert | O(log n) |
| Pop/Extract | O(log n) |
| Peek | O(1) |
| Heapify | O(n) |

## Common Interview Questions
1. **Kth Largest Element in an Array**:  Use a Min-Heap of size K.
2. **K Closest Points to Origin**:  Use a Max-Heap of size K.
3. **Task Scheduler**:  Use a Max-Heap to always pick the most frequent task.
4. **Find Median from Data Stream**:  Use two heaps (a Max-Heap and a Min-Heap).

## Role-Specific Applications
- **Frontend**: Priority-based rendering tasks, managing event queues with priorities.
- **Backend**: Job scheduling (e.g., Celery, Sidekiq), Load balancing (Least connections), Dijkstra's algorithm.
- **ML/Data**: K-Nearest Neighbors (KNN) optimization, selecting top features.
- **DevOps**: Managing priority-based alerts, resource scheduling in orchestrators like Kubernetes.

## Related Topics
- [[01_Foundations/01_DSA/Trees/Index|Trees]]
- [[01_Foundations/01_DSA/Graphs/Index|Graphs]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Heap & Priority Queue Tag](https://leetcode.com/tag/heap-priority-queue/)
