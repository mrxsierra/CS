---
type: concept
tags: [foundations, dsa, two-pointers]
created: 2024-06-10
---

# Two Pointers

## Overview
The Two Pointers pattern is a technique where two pointers (indices) iterate through a data structure (usually an array or a linked list) to find a pair or a range that satisfies a certain condition. It is often used to optimize O(n²) solutions to O(n).

## Key Principles & Patterns
- **Opposite Ends**: Pointers start at the beginning and end, moving toward each other. Typically used for sorted arrays (e.g., Two Sum II, Palindrome).
- **Same Direction (Slow/Fast)**: One pointer moves faster than the other. Often used for cycle detection or finding the middle of a linked list (Floyd's Cycle-Finding Algorithm).
- **Fixed Gap**: Two pointers move in the same direction with a fixed distance between them. Used for finding the Nth node from the end.

## Complexity Analysis
- **Time**: Typically **O(n)** because each pointer traverses the data structure at most once.
- **Space**: **O(1)** as it only requires a few extra variables for the pointers.

## Common Interview Questions
1. **Valid Palindrome**: Start pointers at both ends and compare characters while moving toward the center.
2. **Two Sum II (Sorted Array)**: If sum > target, move right pointer left; if sum < target, move left pointer right.
3. **3Sum**: Sort the array, then for each element, use the Two Pointers (Opposite Ends) approach on the remaining subarray to find pairs that sum to the negative of the current element.
4. **Container With Most Water**: Pointers at ends, calculate area, move the pointer pointing to the shorter line.
5. **Trapping Rain Water**: Use two pointers to track left and right max heights while calculating trapped water.

## Role-Specific Applications
- **Frontend**: Optimizing UI rendering for large datasets, efficient search in sorted lists.
- **Backend**: Data processing in sorted streams, merging sorted datasets, sequence alignment.
- **ML/Data**: Preprocessing sequential data, finding specific patterns or anomalies in time-series data.
- **DevOps**: Log file analysis, comparing two sorted versions of configuration files.

## Related Topics
- [[01_foundations/01_dsa/arrays_and_hashing/index|Arrays & Hashing]]
- [[01_foundations/01_dsa/sliding_window/index|Sliding Window]]
- [[01_foundations/01_dsa/linked_lists/index|Linked Lists]]

## Resources
- [NeetCode Roadmap - Two Pointers](https://neetcode.io/roadmap)
- [Blind 75 List](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)
