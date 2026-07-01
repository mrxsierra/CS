---
type: concept
tags: [foundations, dsa, stack]
created: 2024-06-10
---

# Stack

## Overview
A Stack is a LIFO (Last-In-First-Out) data structure. It's often used for problems involving nested structures or maintaining a specific order of elements.

## Key Principles & Patterns
- LIFO Property: The last element added is the first one removed.
- Monotonic Stack: A stack that maintains elements in increasing or decreasing order. Used to find the 'next greater/smaller' element.
- Recursion Simulation: Any recursive algorithm can be implemented iteratively using a stack.

## Complexity Analysis
| Operation | Complexity |
|-----------|------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |

## Common Interview Questions
1. **Valid Parentheses**:  Use a stack to match opening and closing brackets.
2. **Min Stack**:  Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.
3. **Daily Temperatures**:  Use a monotonic stack to find the next warmer day in O(n).
4. **Evaluate Reverse Polish Notation**:  Use a stack to store operands and apply operators.

## Role-Specific Applications
- **Frontend**: Managing navigation history (browser back/forward), undo/redo functionality.
- **Backend**: Expression evaluation in compilers, managing function calls (Call Stack), parsing nested formats (JSON/XML).
- **ML/Data**: Processing tree-based models or recursive data structures.
- **DevOps**: Parsing configuration files with nested blocks, trace analysis.

## Related Topics
- [[01_foundations/01_dsa/trees/index|Trees]]
- [[01_foundations/01_dsa/graphs/index|Graphs]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Stack Tag](https://leetcode.com/tag/stack/)
