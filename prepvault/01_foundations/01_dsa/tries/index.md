---
type: concept
tags: [foundations, dsa, tries]
created: 2024-06-10
---

# Tries

## Overview
A Trie (Prefix Tree) is a special type of tree used to store associative data structures. A common application is storing strings.

## Key Principles & Patterns
- Character Nodes: Each node represents a character of a string.
- Prefix Matching: Very efficient for searching all strings with a common prefix.
- End of Word Marker: Boolean flag to indicate the completion of a word.

## Complexity Analysis
| Operation | Complexity |
|-----------|------------|
| Insert | O(L) |
| Search | O(L) |
| StartsWith | O(L) |
*(L = length of word)*

## Common Interview Questions
1. **Implement Trie**:  Define Insert, Search, and StartsWith methods.
2. **Design Add and Search Words Data Structure**:  Handle '.' for wildcard matching using DFS.
3. **Word Search II**:  Use a Trie to efficiently search for multiple words in a 2D grid.

## Role-Specific Applications
- **Frontend**: Autofill/Autosuggest features in search bars, spell checkers.
- **Backend**: IP routing (Longest Prefix Match), implementing dictionary-based compression.
- **ML/Data**: Natural Language Processing (NLP) tasks, keyword extraction.
- **DevOps**: Efficient storage and retrieval of hierarchical config keys or log prefixes.

## Related Topics
- [[01_foundations/01_dsa/trees/index|Trees]]
- [[01_foundations/01_dsa/graphs/index|Graphs]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Tries Tag](https://leetcode.com/tag/tries/)
