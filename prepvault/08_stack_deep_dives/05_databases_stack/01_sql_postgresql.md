---
title: PostgreSQL & SQL Mastery
tags: ['stack/databases']
created: 2026-06-10
---

# PostgreSQL & SQL Mastery

## Overview
SQL is the #1 skill tested across backend, data engineering, and even PM interviews. You need to go beyond `SELECT * FROM users` — master window functions, query optimization, and PostgreSQL internals.

## Core SQL — Beyond the Basics

### Window Functions
Window functions perform calculations across a set of rows related to the current row — **without collapsing them** into a single output row.

```sql
-- RANK vs DENSE_RANK vs ROW_NUMBER
SELECT 
  name, 
  salary,
  ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num,  -- 1, 2, 3, 4 (no ties)
  RANK() OVER (ORDER BY salary DESC) as rank,            -- 1, 1, 3, 4 (ties skip)
  DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank -- 1, 1, 2, 3 (no gaps)
FROM employees;

-- LAG / LEAD — access previous/next row
SELECT 
  date,
  revenue,
  LAG(revenue, 1) OVER (ORDER BY date) as prev_day_revenue,
  revenue - LAG(revenue, 1) OVER (ORDER BY date) as daily_change
FROM daily_revenue;

-- PARTITION BY — reset window per group
SELECT 
  department,
  name,
  salary,
  AVG(salary) OVER (PARTITION BY department) as dept_avg,
  salary - AVG(salary) OVER (PARTITION BY department) as above_avg
FROM employees;
```

### Common Table Expressions (CTEs)
```sql
-- Recursive CTE: Employee hierarchy
WITH RECURSIVE org_tree AS (
  SELECT id, name, manager_id, 1 as depth
  FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, t.depth + 1
  FROM employees e
  JOIN org_tree t ON e.manager_id = t.id
)
SELECT * FROM org_tree;
```

### The "Consecutive Days" Problem (Classic)
```sql
-- Find users who logged in for 3+ consecutive days
WITH login_groups AS (
  SELECT 
    user_id, 
    login_date,
    login_date - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date)::int as group_id
  FROM logins
)
SELECT user_id, MIN(login_date) as streak_start, COUNT(*) as streak_length
FROM login_groups
GROUP BY user_id, group_id
HAVING COUNT(*) >= 3;
```

## PostgreSQL Internals

### Index Types
| Index Type | Best For | Example |
|-----------|----------|---------|
| **B-Tree** (default) | Equality + Range queries, sorting | `CREATE INDEX ON users (email)` |
| **Hash** | Equality lookups only | `CREATE INDEX ON users USING HASH (id)` |
| **GIN** | Arrays, JSONB, full-text search | `CREATE INDEX ON posts USING GIN (tags)` |
| **GiST** | Geometric data, full-text (ranking) | `CREATE INDEX ON locations USING GIST (coord)` |
| **BRIN** | Large tables with naturally ordered data (time-series) | `CREATE INDEX ON logs USING BRIN (created_at)` |

### Query Execution Plan
```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';
-- Shows: Seq Scan vs. Index Scan, actual time, rows, cost
```
- **Seq Scan** — Full table scan (bad for large tables without index)
- **Index Scan** — Index look-up + heap fetch (good)
- **Index Only Scan** — All needed data in index (best)
- **Bitmap Heap Scan** — Multiple index lookups merged (good for complex filters)

### ACID & Isolation Levels
| Level | Dirty Read | Non-repeatable Read | Phantom Read |
|-------|-----------|-------------------|-------------|
| Read Uncommitted | ❌ Possible | Possible | Possible |
| Read Committed (default) | ✅ Prevented | Possible | Possible |
| Repeatable Read | ✅ Prevented | ✅ Prevented | Possible |
| Serializable | ✅ Prevented | ✅ Prevented | ✅ Prevented |

### MVCC (Multi-Version Concurrency Control)
PostgreSQL doesn't lock rows for reads — it keeps multiple versions of each row:
- `INSERT` creates a new row version
- `UPDATE` marks old row as dead + creates new version
- `DELETE` marks row as dead
- `VACUUM` reclaims storage from dead rows

## Interview Questions

1. **"What's the difference between `WHERE` and `HAVING`?"** — `WHERE` filters rows before aggregation; `HAVING` filters after `GROUP BY`.

2. **"When would you use a CTE vs. a subquery?"** — CTEs are readable, reusable, can be recursive. Subqueries can sometimes be optimized better by the planner.

3. **"How do you optimize a slow query?"** — Check `EXPLAIN ANALYZE` for Seq Scans → add indexes. Check for N+1 queries → use JOINs. Check for full table sorts → add index on sort column.

4. **"What is a deadlock? How do you resolve it?"** — Two transactions waiting for each other's locks. Solution: Access tables/rows in a consistent order, or set a lock timeout.

## Related Topics
- [[08_stack_deep_dives/05_databases_stack/02_mongodb_nosql|MongoDB & NoSQL]]
- [[08_stack_deep_dives/05_databases_stack/03_redis_caching|Redis & Caching]]
- [[08_stack_deep_dives/05_databases_stack/index|Databases Stack Index]]
- [[01_foundations/10_sql_database_deep_dive|SQL Database Deep Dive]]

## Resources
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Use the Index, Luke](https://use-the-index-luke.com/)
- [PG Exercises](https://pgexercises.com/)