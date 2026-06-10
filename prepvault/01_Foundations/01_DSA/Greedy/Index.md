---
type: concept
tags: [foundations, dsa, greedy]
created: 2024-06-10
---

# Greedy

## Overview
A greedy algorithm makes the locally optimal choice at each step with the hope of finding a global optimum.

## Key Principles & Patterns
- Greedy Choice Property: A global optimum can be reached by making a local optimum.
- No Backtracking: Once a choice is made, it is never changed.
- Sorting: Greedy problems often involve sorting the input first.

## Complexity Analysis
Usually dominated by sorting: O(n log n).

## Common Interview Questions
1. **Jump Game**:  Track the maximum reachable index.
2. **Gas Station**:  Determine if you can complete a circuit.
3. **Hand of Straights**:  Use a Hash Map to count frequencies and always start from the smallest card.
4. **Partition Labels**:  Find the last occurrence of each character to determine partition boundaries.

## Role-Specific Applications
- **Frontend**: Simple layout engines, heuristic-based UI rendering.
- **Backend**: Huffman coding for compression, Prim's/Kruskal's algorithms for Minimum Spanning Tree.
- **ML/Data**: Decision tree splits, feature selection (stepwise regression).
- **DevOps**: Basic load balancing (Round Robin), task scheduling with simple priorities.

## Related Topics
- [[01_Foundations/01_DSA/Dynamic Programming/Index|Dynamic Programming]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Greedy Tag](https://leetcode.com/tag/greedy/)
