---
type: concept
tags: [foundations, sql, databases, indexing, transactions]
created: 2026-06-10
---

# SQL Database Deep Dive

Modern technical interviews (Backend/Data) frequently probe deep into relational database internals. This guide covers the critical areas you need to master.

---

## 1. ACID Transactions
A transaction is a single unit of work. To ensure data integrity, RDBMS must support ACID properties:
- **Atomicity**: All changes are committed, or none are.
- **Consistency**: Data must follow all schema rules (constraints, triggers).
- **Isolation**: Concurrent transactions don't interfere with each other.
- **Durability**: Committed data is permanent, even after a crash.

### Isolation Levels (Standard SQL)
1. **Read Uncommitted**: Lowest level; allows "Dirty Reads".
2. **Read Committed**: Prevents dirty reads; allowed in most production environments.
3. **Repeatable Read**: Prevents "Non-repeatable Reads"; MySQL default.
4. **Serializable**: Highest level; prevents "Phantom Reads" via range locks.

---

## 2. Indexing Internals (B-Trees)
Most SQL indexes use **B+ Trees**.
- **Structure**: Root -> Branch -> Leaf. Leaf nodes are linked together for fast range scans.
- **Clustered Index**: The actual data is stored in the leaf nodes of the B+ Tree (usually the Primary Key).
- **Non-Clustered (Secondary) Index**: Stores the index key and a pointer to the clustered index record.

### Indexing Strategies
- **Covering Index**: An index that contains all the columns required by a query, allowing the database to skip reading the actual data table.
- **Composite Index**: An index on multiple columns. Order matters! (Follow the "Leftmost Prefix" rule).

---

## 3. Query Optimization
Interviewer: *"This query is slow. How do you fix it?"*

1. **EXPLAIN ANALYZE**: Check the execution plan. Look for "Sequential Scan" (bad for large tables) vs. "Index Scan" (good).
2. **Check for missing indexes**: Are the `WHERE` and `JOIN` columns indexed?
3. **N+1 Query Problem**: Are you fetching 100 items and then doing 100 individual queries for their metadata? Use `JOIN` or `IN`.
4. **Avoid `SELECT *`**: Fetch only the columns you need to reduce I/O.

---

## 4. Normalization vs. Denormalization
- **Normalization (1NF, 2NF, 3NF)**: Reducing redundancy. Good for **Write-heavy** applications (OLTP).
- **Denormalization**: Intentionally adding redundancy to speed up reads. Good for **Read-heavy** or Analytical applications (OLAP).

---

## 5. Modern SQL: Window Functions
Essential for Data Engineering/Analytics interviews.
```sql
SELECT 
    user_id, 
    score,
    RANK() OVER (ORDER BY score DESC) as rank,
    AVG(score) OVER (PARTITION BY department_id) as dept_avg
FROM employees;
```

---

## Role-Specific Applications
- **[[02_role_tracks/03_backend_engineer|Backend]]**: Handling race conditions with row-level locking, optimizing API performance via indexing.
- **[[02_role_tracks/06_data_engineer|Data Engineering]]**: Designing star schemas, optimizing ETL batch loads, partitioning large tables.
- **[[02_role_tracks/10_data_analyst|Data Analyst]]**: Writing complex window functions and CTEs for business reporting.

## Related Topics
- [[01_foundations/03_system_design|System Design (Sharding/Replication)]]
- [[08_stack_deep_dives/05_databases_stack/index|Database Stack]]
