---
type: concept
tags: [foundations, dsa, intervals]
created: 2024-06-10
---

# Intervals

## Overview
Interval problems deal with ranges of values, usually represented as `[start, end]`. Sorting is almost always the first step.

## Key Principles & Patterns
- Sorting: Sort by start time (most common) or end time.
- Overlaps: Two intervals [s1, e1] and [s2, e2] overlap if `max(s1, s2) < min(e1, e2)`.
- Merging: If intervals overlap, their merged range is `[min(s1, s2), max(e1, e2)]`.

## Complexity Analysis
Usually O(n log n) due to sorting.

## Common Interview Questions
1. **Merge Intervals**:  Sort and merge overlapping intervals.
2. **Insert Interval**:  Insert a new interval and merge it with existing ones.
3. **Non-overlapping Intervals**:  Find the minimum number of intervals to remove (Greedy approach).
4. **Meeting Rooms II**:  Find the maximum number of concurrent meetings (using a Heap or sorting start/end times).

## Role-Specific Applications
- **Frontend**: Calendar UI rendering, detecting overlaps in draggable components.
- **Backend**: Scheduling systems, booking platforms (hotels, flights), range-based queries in databases.
- **ML/Data**: Temporal data analysis, processing time series with gaps.
- **DevOps**: Monitoring uptime windows, analyzing overlapping log events from multiple services.

## Related Topics
- [[01_foundations/01_dsa/arrays_and_hashing/index|Arrays & Hashing]]
- [[01_foundations/01_dsa/greedy/index|Greedy]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Intervals Tag](https://leetcode.com/tag/intervals/)
