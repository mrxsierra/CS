---
type: concept
tags: [foundations, dsa, linked-lists]
created: 2024-06-10
---

# Linked Lists

## Overview
A Linked List is a linear data structure where elements are not stored at contiguous memory locations. Each element (node) points to the next.

## Key Principles & Patterns
- Nodes and Pointers: Each node contains data and a 'next' reference.
- Dummy Nodes: Using a placeholder node at the head to simplify edge cases (like deleting the head).
- Two Pointers (Fast & Slow): Used for cycle detection and finding the middle element.
- Reverse: Standard pattern to reverse pointers in-place.

## Complexity Analysis
| Operation | Complexity |
|-----------|------------|
| Access | O(n) |
| Search | O(n) |
| Insert/Delete | O(1) (with pointer) |

## Common Interview Questions
1. **Reverse Linked List**:  Iterative and recursive approaches.
2. **Merge Two Sorted Lists**:  Use a dummy node and a recursive or iterative approach.
3. **Linked List Cycle**:  Use Floyd's Cycle-Finding Algorithm (Fast & Slow pointers).
4. **Remove Nth Node From End**:  Use two pointers with a gap of N.
5. **Reorder List**:  Combine finding the middle, reversing the second half, and merging.

## Role-Specific Applications
- **Frontend**: Implementing undo/redo, managing layers in graphics software, DOM tree manipulation (nodes have siblings/parents).
- **Backend**: Implementing LRU Caches (Hash Map + Doubly Linked List), handling collisions in Hash Maps (Chaining).
- **ML/Data**: Representing sparse data, stream processing where elements are processed sequentially.
- **DevOps**: Process scheduling (Circular Linked Lists), managing free memory blocks.

## Related Topics
- [[01_Foundations/01_DSA/Two Pointers/Index|Two Pointers]]
- [[01_Foundations/01_DSA/Stack/Index|Stack]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Linked Lists Tag](https://leetcode.com/tag/linked-lists/)
