---
type: concept
tags: [foundations, dsa, graphs]
created: 2024-06-10
---

# Graphs

## Overview
A Graph consists of vertices (nodes) and edges. They can be directed/undirected and weighted/unweighted.

## Key Principles & Patterns
- Adjacency List/Matrix: Ways to represent a graph in code.
- BFS: Used for shortest path in unweighted graphs.
- DFS: Used for connectivity, cycle detection, and topological sort.
- Union Find: Efficient for tracking connected components.
- Topological Sort: Linear ordering of vertices for Directed Acyclic Graphs (DAG).

## Complexity Analysis
| Algorithm | Complexity |
|-----------|------------|
| BFS/DFS | O(V + E) |
| Dijkstra | O(E log V) |
| Topological Sort | O(V + E) |

## Common Interview Questions
1. **Number of Islands**:  Use BFS or DFS to traverse connected '1's.
2. **Course Schedule**:  Use Topological Sort (Kahn's Algorithm) to detect cycles.
3. **Clone Graph**:  Use DFS/BFS with a Hash Map to keep track of cloned nodes.
4. **Pacific Atlantic Water Flow**:  Multi-source DFS/BFS starting from the oceans.
5. **Network Delay Time**:  Use Dijkstra's algorithm for shortest path in a weighted graph.

## Role-Specific Applications
- **Frontend**: Representing social networks, state machines in complex UI logic, dependency graphs in build tools (Webpack/Vite).
- **Backend**: Recommendation engines, pathfinding in maps (Google Maps), modeling microservice dependencies.
- **ML/Data**: Knowledge Graphs, Graph Neural Networks (GNNs), PageRank algorithm.
- **DevOps**: Infrastructure mapping, service mesh visualization, CI/CD pipeline dependencies.

## Related Topics
- [[01_foundations/01_dsa/trees/index|Trees]]
- [[01_foundations/01_dsa/heap_and_priority_queue/index|Heap & Priority Queue]]

## Resources
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode Graphs Tag](https://leetcode.com/tag/graphs/)
