---
type: concept
tags: [foundations, dsa, dynamic-programming]
created: 2024-06-10
---

# Dynamic Programming

## Overview
DP is an optimization over plain recursion. It involves breaking down a problem into subproblems and storing the results (Memoization or Tabulation).

## Key Principles & Patterns
- Optimal Substructure: The optimal solution to the problem contains optimal solutions to subproblems.
- Overlapping Subproblems: The same subproblems are solved multiple times.
- Memoization (Top-Down): Storing results in a Hash Map or array during recursion.
- Tabulation (Bottom-Up): Filling a table (usually an array or matrix) iteratively.

## Complexity Analysis
Varies by problem, but usually reduces O(2^n) to O(n^2) or O(n).

## Common Interview Questions
1. **Climbing Stairs**:  Fibonacci sequence pattern solved with DP.
2. **Coin Change**:  Find the minimum number of coins to reach a target sum.
3. **Longest Increasing Subsequence**:  Standard DP problem O(n^2) or O(n log n).
4. **House Robber**:  Simple linear DP with state transition `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.
5. **Longest Common Subsequence**:  2D DP problem for string comparison.

## Role-Specific Applications
- **Frontend**: Diffing algorithms, optimizing heavy computations (memoization in React's `useMemo`).
- **Backend**: Query optimization, resource allocation, string matching (diff tools), sequence alignment in bioinformatics.
- **ML/Data**: Viterbi algorithm in HMMs, Reinforcement Learning (Bellman equations).
- **DevOps**: Cost optimization for cloud resources, path optimization in complex networks.

## Related Topics
- [[01_Foundations/01_DSA/Greedy/Index|Greedy]]
- [[01_Foundations/01_DSA/Recursion/Index|Recursion]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Dynamic Programming Tag](https://leetcode.com/tag/dynamic-programming/)
