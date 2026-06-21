---
type: concept
tags: [foundations, dsa, backtracking, recursion]
created: 2026-06-10
---

# Backtracking

## Overview
Backtracking is a refined brute-force approach. It involves building a solution incrementally and removing solutions that fail to satisfy the constraints of the problem at any point in time. It is essentially a DFS on the state-space tree of the problem.

## Key Principles & Patterns
- **Choice, Constraint, Goal**: 
    - **Choice**: What decision do we make at this step?
    - **Constraint**: Is this choice valid?
    - **Goal**: Have we reached a complete solution?
- **State Reset (The "Backtrack")**: After exploring a path, you must undo the last choice to return to the previous state and try other options.
- **Pruning**: Cutting off branches of the search tree that cannot possibly lead to a valid solution.

## Complexity Analysis
- **Time**: Often exponential **O(2^N)**, **O(N!)**, or **O(K^N)** depending on the number of choices at each step.
- **Space**: **O(N)** for the recursion stack (the depth of the tree).

## Common Interview Questions
1. **Subsets**: Find all possible subsets of a set (Power Set).
2. **Permutations**: Find all possible arrangements of a list of numbers.
3. **Combination Sum**: Find all unique combinations of candidates that sum to a target.
4. **N-Queens**: Place N queens on an NxN chessboard such that no two queens attack each other.
5. **Word Search**: Find if a word exists in a 2D grid by moving in 4 directions.

## Role-Specific Applications
- **Frontend**: Parsing nested JSON/XML for UI trees, resolving complex component dependencies.
- **Backend**: Resource allocation algorithms, solving constraint satisfaction problems (e.g., scheduling), pathfinding in complex networks.
- **ML/Data**: Decision tree construction, feature selection (searching through subset combinations).
- **DevOps**: Dependency resolution in package managers or infrastructure graphs (Terraform plan).

## Related Topics
- [[01_Foundations/01_DSA/Graphs/Index|Graphs (DFS)]]
- [[01_Foundations/01_DSA/Stack/Index|Stack (Recursion)]]

## Resources
- [NeetCode Roadmap - Backtracking](https://neetcode.io/roadmap)
- [LeetCode Backtracking Tag](https://leetcode.com/tag/backtracking/)
