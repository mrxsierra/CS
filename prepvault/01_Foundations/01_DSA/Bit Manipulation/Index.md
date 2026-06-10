---
type: concept
tags: [foundations, dsa, bit-manipulation]
created: 2024-06-10
---

# Bit Manipulation

## Overview
Bit manipulation involves operating on the binary representation of data. It is often used for performance optimization and low-level data handling.

## Key Principles & Patterns
- Basic Operators: AND (&), OR (|), XOR (^), NOT (~), Left Shift (<<), Right Shift (>>).
- XOR Property: `a ^ a = 0` and `a ^ 0 = a`. Used to find unique elements.
- Bit Masks: Using an integer to represent a set of boolean flags.
- Checking/Setting Bits: `(n >> i) & 1` to check the i-th bit.

## Complexity Analysis
O(1) or O(number of bits, usually 32 or 64).

## Common Interview Questions
1. **Number of 1 Bits**:  Count the number of set bits (Hamming Weight).
2. **Counting Bits**:  Use DP with bit manipulation to count bits for a range of numbers.
3. **Missing Number**:  Use XOR to find the missing number in an array of 0..n.
4. **Sum of Two Integers**:  Implement addition without using `+` or `-` using XOR and AND.
5. **Reverse Bits**:  Reverse the binary representation of an integer.

## Role-Specific Applications
- **Frontend**: Handling binary data (TypedArrays, Blobs), optimizing flags in complex state.
- **Backend**: Permissions/Roles (Bitmasks), network protocols, data compression, encryption.
- **ML/Data**: Feature hashing, optimizing storage for large boolean datasets.
- **DevOps**: Subnet masking, file permissions (chmod), compacting log data.

## Related Topics
- [[01_Foundations/01_DSA/Arrays & Hashing/Index|Arrays & Hashing]]
- [[01_Foundations/01_DSA/Math & Geometry/Index|Math & Geometry]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Bit Manipulation Tag](https://leetcode.com/tag/bit-manipulation/)
