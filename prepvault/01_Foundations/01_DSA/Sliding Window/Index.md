---
type: concept
tags: [foundations, dsa, sliding-window]
created: 2024-06-10
---

# Sliding Window

## Overview
The Sliding Window pattern is used to perform a required operation on a specific window size of a given array or linked list, such as finding the longest subarray containing all 1s.

## Key Principles & Patterns
- Fixed Window: The window size is constant. We slide it across the array.
- Variable Window: The window size changes based on certain conditions (e.g., sum of elements).
- State Tracking: Using a Hash Map or variables to track the state within the current window.

## Complexity Analysis
| Type | Time | Space |
|------|------|-------|
| Fixed | O(n) | O(1) |
| Variable | O(n) | O(k) or O(1) |

## Common Interview Questions
1. **Best Time to Buy and Sell Stock**:  Single pass O(n) sliding window to find max profit.
2. **Longest Substring Without Repeating Characters**:  Variable window with Hash Map to track character indices.
3. **Longest Repeating Character Replacement**:  Track frequency of most frequent character in the window.

## Role-Specific Applications
- **Frontend**: Implementing virtualized lists, debouncing/throttling event streams.
- **Backend**: Rate limiting (Sliding Window Log/Counter), network congestion control (TCP sliding window).
- **ML/Data**: Time-series analysis, rolling average calculations, feature engineering for sequential data.
- **DevOps**: Monitoring metrics over time windows, log aggregation within specific timeframes.

## Related Topics
- [[01_Foundations/01_DSA/Arrays & Hashing/Index|Arrays & Hashing]]
- [[01_Foundations/01_DSA/Two Pointers/Index|Two Pointers]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Sliding Window Tag](https://leetcode.com/tag/sliding-window/)
