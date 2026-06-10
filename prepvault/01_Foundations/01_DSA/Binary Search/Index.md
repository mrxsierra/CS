---
type: concept
tags: [foundations, dsa, binary-search]
created: 2024-06-10
---

# Binary Search

## Overview
Binary Search is an efficient O(log n) algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item.

## Key Principles & Patterns
- Sorted Input: The input must be sorted or have a property that allows discarding half of the search space.
- Search Space: Binary Search isn't just for arrays; it can be used on a range of integers (Binary Search on Answer).
- Left, Right, Mid: Careful handling of pointers to avoid infinite loops (e.g., `left <= right` and `mid = left + (right - left) // 2`).

## Complexity Analysis
| Operation | Complexity |
|-----------|------------|
| Search | O(log n) |
| Space | O(1) |

## Common Interview Questions
1. **Search a 2D Matrix**:  Treat the 2D matrix as a 1D sorted array.
2. **Koko Eating Bananas**:  Binary search on the 'speed' of eating bananas.
3. **Find Minimum in Rotated Sorted Array**:  Binary search to find the inflection point.
4. **Search in Rotated Sorted Array**:  Determine which half is sorted and adjust pointers.

## Role-Specific Applications
- **Frontend**: Optimizing search in large client-side datasets, finding position for inserted elements in sorted lists.
- **Backend**: Database indexing (B-Trees use binary search internally), searching logs by timestamp.
- **ML/Data**: Hyperparameter tuning (Grid/Random search can be optimized), threshold optimization.
- **DevOps**: Git bisect for finding buggy commits, binary search for identifying problematic config ranges.

## Related Topics
- [[01_Foundations/01_DSA/Arrays & Hashing/Index|Arrays & Hashing]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Binary Search Tag](https://leetcode.com/tag/binary-search/)
