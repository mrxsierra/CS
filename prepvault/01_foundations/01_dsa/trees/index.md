---
type: concept
tags: [foundations, dsa, trees]
created: 2024-06-10
---

# Trees

## Overview
A Tree is a hierarchical data structure consisting of nodes, with a single root node. Binary Trees are most common in interviews.

## Key Principles & Patterns
- Recursion: The most natural way to solve tree problems.
- DFS (Depth-First Search): Pre-order, In-order, Post-order traversals.
- BFS (Breadth-First Search): Level-order traversal using a Queue.
- BST (Binary Search Tree): Left < Root < Right property. In-order traversal of BST is sorted.

## Complexity Analysis
| Operation | Average | Worst (Skewed) |
|-----------|---------|----------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

## Common Interview Questions
1. **Invert Binary Tree**:  Recursive swap of left and right children.
2. **Maximum Depth of Binary Tree**:  Recursive DFS or level-order BFS.
3. **Binary Tree Level Order Traversal**:  Standard BFS using a queue.
4. **Kth Smallest Element in BST**:  In-order traversal until the kth element.
5. **Lowest Common Ancestor**:  Find the split point in a BST or use recursion for general trees.

## Role-Specific Applications
- **Frontend**: The DOM (Document Object Model) is a tree, Virtual DOM diffing algorithms (React).
- **Backend**: File systems (directory structure), Database indexing (B/B+ Trees), Abstract Syntax Trees (AST) in compilers.
- **ML/Data**: Decision Trees, Random Forests, Gradient Boosting Machines.
- **DevOps**: Managing hierarchical infrastructure (e.g., Kubernetes resource hierarchy), DNS (Domain Name System).

## Related Topics
- [[01_foundations/01_dsa/graphs/index|Graphs]]
- [[01_foundations/01_dsa/tries/index|Tries]]
- [[01_foundations/01_dsa/heap_and_priority_queue/index|Heap & Priority Queue]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Trees Tag](https://leetcode.com/tag/trees/)
