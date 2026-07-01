---
type: concept
tags: [foundations, dsa, arrays-hashing]
created: 2024-06-10
---

# Arrays & Hashing

## Overview
Arrays and Hashing are the most fundamental building blocks in DSA. Arrays provide sequential storage with O(1) access, while Hashing (Hash Maps/Sets) enables O(1) average-case lookups, insertions, and deletions by mapping keys to indices.

## Key Principles & Patterns
- **Fixed vs. Dynamic Arrays**: Understanding how dynamic arrays (e.g., `ArrayList` in Java, `vector` in C++, `list` in Python) resize (usually doubling capacity) and the amortized O(1) cost of appending.
- **Hash Map/Set**: Using a hash function to map keys to a bucket. Handling collisions (Chaining vs. Open Addressing).
- **Prefix Sum**: Precomputing sums of subarrays to answer range sum queries in O(1).
- **Two-Pass Hashing**: First pass to count frequencies, second pass to find the result (e.g., First Unique Character).
- **Sliding Window (Static)**: Using a fixed-size window over an array to find optimal subarrays.

## Complexity Analysis
| Operation | Array (Static) | Hash Map (Average) |
|-----------|----------------|--------------------|
| Access    | O(1)           | O(1)               |
| Search    | O(n)           | O(1)               |
| Insertion | O(n)           | O(1)               |
| Deletion  | O(n)           | O(1)               |

## Common Interview Questions
1. **Two Sum**: Use a Hash Map to store seen numbers and their indices to find the complement in O(n).
2. **Contains Duplicate**: Use a Hash Set to check for seen elements in O(n).
3. **Valid Anagram**: Use a frequency counter (Hash Map or array of size 26) to compare character counts.
4. **Group Anagrams**: Use a sorted string or character count tuple as a Hash Map key.
5. **Top K Frequent Elements**: Use a Hash Map for counting and then a Heap or Bucket Sort for retrieval.

## Role-Specific Applications
- **Frontend**: Managing state in UI frameworks (e.g., React's `useState` with arrays), efficient lookups for normalized state in Redux.
- **Backend**: Database indexing (B-Trees vs. Hash Indexes), Caching mechanisms (LRU Cache uses Hash Map + Double Linked List).
- **ML/Data**: NumPy arrays for vectorization, Hash functions for feature hashing and dimensionality reduction.
- **DevOps**: Log parsing and frequency analysis, load balancing (Consistent Hashing).

## Related Topics
- [[01_foundations/01_dsa/two_pointers/index|Two Pointers]]
- [[01_foundations/01_dsa/sliding_window/index|Sliding Window]]

## Resources
- [NeetCode Roadmap - Arrays & Hashing](https://neetcode.io/roadmap)
- [Blind 75 List](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)
