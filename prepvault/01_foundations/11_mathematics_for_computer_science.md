---
title: Mathematics for Computer Science (Discrete Math)
tags: [foundations/math, foundations/logic, foundations/combinatorics, foundations/probability, foundations/graph-theory]
created: 2026-06-23
---

# Mathematics for Computer Science: Discrete Math Masterclass

Discrete Mathematics is the backbone of Computer Science. Unlike calculus, which deals with continuous change, discrete math deals with distinct, countable objects. It provides the theoretical framework for data structures, algorithms, cryptography, and system design.

---

## 1. Propositional & Predicate Logic

Logic is the basis of circuit design, programming languages, and formal verification.

### 1.1 Propositional Logic
- **Propositions**: Statements that are either True (T) or False (F).
- **Logical Connectives**:
    - **NOT ($\neg$p)**: Flips the truth value.
    - **AND (p $\land$ q)**: T only if both are T.
    - **OR (p $\lor$ q)**: T if at least one is T.
    - **XOR (p $\oplus$ q)**: T if exactly one is T.
    - **IMPLIES (p $\rightarrow$ q)**: F only if p is T and q is F. (Equivalent to $\neg$p $\lor$ q).
    - **Biconditional (p $\leftrightarrow$ q)**: T if both have the same truth value.

### 1.2 Logical Equivalences
- **De Morgan’s Laws**:
    - $\neg(p \land q) \equiv \neg p \lor \neg q$
    - $\neg(p \lor q) \equiv \neg p \land \neg q$
- **Distributive Laws**:
    - $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$
    - $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$

### 1.3 Predicate Logic (First-Order Logic)
- **Quantifiers**:
    - **Universal Quantifier ($\forall x P(x)$)**: "For all x, P(x) is true."
    - **Existential Quantifier ($\exists x P(x)$)**: "There exists an x such that P(x) is true."
- **Negation of Quantifiers**:
    - $\neg \forall x P(x) \equiv \exists x \neg P(x)$
    - $\neg \exists x P(x) \equiv \forall x \neg P(x)$

### 1.4 Boolean Algebra in CS
- Used in **Bit Manipulation** and **Compiler Optimization**.
- **CNF (Conjunctive Normal Form)**: AND of ORs (e.g., $(A \lor B) \land (\neg A \lor C)$).
- **DNF (Disjunctive Normal Form)**: OR of ANDs (e.g., $(A \land B) \lor (\neg A \land C)$).

---

## 2. Set Theory & Relations

Sets are the foundation for data structures like `HashSet` and `HashMap`.

### 2.1 Set Basics
- **Cardinality ($|S|$)**: The number of elements in a set.
- **Power Set ($\mathcal{P}(S)$)**: The set of all subsets. If $|S| = n$, then $|\mathcal{P}(S)| = 2^n$.
- **Set Operations**: Union ($\cup$), Intersection ($\cap$), Difference ($-$), Complement ($\bar{S}$).

### 2.2 Binary Relations
A relation $R$ from $A$ to $B$ is a subset of $A \times B$.
- **Reflexive**: $\forall a \in A, (a, a) \in R$.
- **Symmetric**: $(a, b) \in R \rightarrow (b, a) \in R$.
- **Transitive**: $(a, b) \in R \land (b, c) \in R \rightarrow (a, c) \in R$.
- **Equivalence Relation**: A relation that is reflexive, symmetric, and transitive. It partitions a set into **Equivalence Classes**.

### 2.3 Partial Orders (Posets)
- A relation that is reflexive, **anti-symmetric**, and transitive.
- **Application**: Task scheduling (DAGs), inheritance hierarchies.
- **Hasse Diagrams**: A visual representation of a poset.

---

## 3. Combinatorics

The art of counting without counting. Essential for analyzing **Time Complexity** and space requirements.

### 3.1 Permutations vs. Combinations
- **Permutations ($P(n, k)$)**: Order matters. $P(n, k) = \frac{n!}{(n-k)!}$
- **Combinations ($C(n, k)$)**: Order does not matter. $C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$

### 3.2 Key Principles
- **Sum Rule**: If tasks are mutually exclusive, add the ways to do them.
- **Product Rule**: If tasks are sequential/independent, multiply the ways.
- **Pigeonhole Principle (PHP)**: If $n$ items are put into $m$ containers, and $n > m$, at least one container has $> 1$ item.
    - *CS Application*: Hash collisions, proving that no lossless compression algorithm can shrink all files.
- **Inclusion-Exclusion Principle**: $|A \cup B| = |A| + |B| - |A \cap B|$.

### 3.3 Binomial Theorem
- $(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k$.
- Connects to **Pascal’s Triangle**.

---

## 4. Graph Theory Foundations

Graphs are everywhere: Social networks, the Internet, file systems, and dependency maps.

### 4.1 Basic Definitions
- **Graph $G = (V, E)$**: $V$ = Vertices, $E$ = Edges.
- **Degree**: Number of edges incident to a vertex. In-degree and out-degree for directed graphs.
- **Isomorphism**: Two graphs are isomorphic if there is a bijection between their vertex sets that preserves adjacency.

### 4.2 Paths and Cycles
- **Euler Path/Cycle**: Uses every **edge** exactly once. (Cycle exists if all vertices have even degree).
- **Hamiltonian Path/Cycle**: Uses every **vertex** exactly once. (Finding one is NP-complete).
- **Bipartite Graph**: Vertices can be partitioned into two sets $U$ and $V$ such that every edge connects a vertex in $U$ to one in $V$. (Equivalent to saying the graph has no odd cycles).

### 4.3 Trees
- A connected acyclic graph.
- **Properties**:
    - $n$ vertices implies $n-1$ edges.
    - Unique path between any two vertices.
    - Adding one edge creates exactly one cycle.

### 4.4 Graph Coloring
- **Vertex Coloring**: Assign colors to vertices such that no two adjacent vertices have the same color.
- **Chromatic Number ($\chi(G)$)**: The minimum colors needed.
- *Application*: Register allocation in compilers, scheduling exams to avoid conflicts.

---

## 5. Discrete Probability

Probability is the key to **Randomized Algorithms** (Quicksort), **Machine Learning**, and **Distributed Systems**.

### 5.1 Basics
- **Sample Space ($S$)**: Set of all possible outcomes.
- **Event ($E$)**: A subset of $S$. $P(E) = \frac{|E|}{|S|}$ for uniform distributions.
- **Conditional Probability**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.

### 5.2 Bayes’ Theorem
- $P(A|B) = \frac{P(B|A) P(A)}{P(B)}$.
- *Application*: Spam filtering, diagnostic tools.

### 5.3 Expected Value
- $E[X] = \sum x P(x)$.
- **Linearity of Expectation**: $E[X + Y] = E[X] + E[Y]$, even if $X$ and $Y$ are dependent.
    - *CS Application*: Average-case analysis of algorithms.

---

## 6. Senior-Level Interview Q&A (Discrete Math Mapping)

### Q1: How do Bloom Filters leverage Set Theory and Probability?
**Answer**: A Bloom Filter is a probabilistic data structure used to test set membership.
- **Logic**: It uses a bit array and $k$ hash functions. To add an element, set bits at indices $h_1(x), ..., h_k(x)$ to 1.
- **Probability**: There is a non-zero probability of a **False Positive** (membership test returns T when element is not in the set) but zero probability of a **False Negative**.
- **Math**: The false positive rate $p$ is approximately $(1 - e^{-kn/m})^k$, where $n$ is elements inserted and $m$ is bit array size. This maps directly to the Bernoulli trial and exponential distribution.

### Q2: How does Graph Theory help in detecting Deadlocks in Operating Systems?
**Answer**: Systems use a **Resource Allocation Graph (RAG)**.
- **Structure**: Vertices represent Processes ($P$) and Resources ($R$). Edges represent "Request" ($P \rightarrow R$) or "Assignment" ($R \rightarrow P$).
- **The Condition**: In a system with single-instance resources, a **cycle** in the graph is a necessary and sufficient condition for deadlock.
- **Mapping**: Deadlock detection is essentially a **Cycle Detection** problem in a directed graph, typically solved via DFS (checking for Back Edges).

### Q3: Why is the "Linearity of Expectation" crucial for Hashing analysis?
**Answer**: In a hash table with $n$ elements and $m$ slots, let $X$ be the number of collisions.
- By defining indicator variables $X_{ij} = 1$ if elements $i$ and $j$ collide, $X = \sum X_{ij}$.
- $E[X] = \sum E[X_{ij}]$. Since $E[X_{ij}] = 1/m$, we calculate $E[X]$ easily even though collisions are not independent.
- This proves that with a good hash function, the average chain length is $O(1 + n/m)$.

### Q4: Explain how B-Trees use the properties of Trees and Combinatorics to optimize DB performance.
**Answer**: B-Trees are balanced $M$-way search trees.
- **Combinatorics**: A node with $k$ keys has $k+1$ children. This high branching factor (fan-out) minimizes the tree height ($h \approx \log_M N$).
- **Performance**: Since disk I/O is the bottleneck, reducing $h$ is critical. Discrete math tells us that for a fixed $N$, increasing $M$ reduces $h$ exponentially.
- **Constraint**: Every node (except root) must be at least half-full, ensuring $O(\log N)$ even in the worst case.

### Q5: How does the Pigeonhole Principle relate to Hash Collisions and Compression?
**Answer**:
- **Hash Collisions**: If your hash output is $b$ bits ($2^b$ possible values) and you hash $2^b + 1$ distinct keys, at least two keys *must* have the same hash.
- **Lossless Compression**: If a compression algorithm makes at least one file smaller, it *must* make at least one other file larger. Why? There are $2^n$ possible files of length $n$. If you map them to a space of smaller files, the Pigeonhole Principle dictates that multiple $n$-length files would map to the same compressed file, making decompression impossible (loss of uniqueness).

---

## Related Topics
- [[01_dsa.md|Data Structures & Algorithms]]
- [[03_system_design.md|System Design]]
- [[04_operating_systems.md|Operating Systems]]
- [[10_sql_database_deep_dive.md|SQL Database Deep Dive]]

## External Resources
- [MIT 6.042J: Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/)
- [Brilliant.org - Discrete Mathematics](https://brilliant.org/wiki/discrete-mathematics/)
- [Book: Discrete Mathematics and Its Applications (Rosen)](https://www.mheducation.com/highered/product/discrete-mathematics-its-applications-rosen/M9781259676512.html)
