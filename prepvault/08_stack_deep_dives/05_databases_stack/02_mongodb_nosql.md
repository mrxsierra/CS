---
title: MongoDB & NoSQL Patterns
tags: ['stack/databases']
created: 2026-06-10
---

# MongoDB & NoSQL Patterns

## Overview
MongoDB is the leading document-oriented NoSQL database. In interviews, you're tested on when to choose NoSQL over SQL, how MongoDB's document model works, and the tradeoffs of its consistency model.

## Document Model — JSON at Rest

### Document Structure
```json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "name": "Alice",
  "email": "alice@example.com",
  "address": {
    "street": "123 Main St",
    "city": "San Francisco"
  },
  "tags": ["engineering", "leadership"],
  "createdAt": ISODate("2026-01-01T00:00:00Z")
}
```

### Embedding vs. Referencing
| Strategy | When to Use | Example |
|----------|-------------|---------|
| **Embedding** | Data accessed together, small/subset relationships | Address in User document |
| **Referencing** | Large/reusable data, many-to-many | User → Posts (user has many posts) |

### The 16MB Document Limit
MongoDB documents are capped at 16MB. If embedding would exceed this (e.g., a user with 10,000 comments), use referencing instead.

## Aggregation Pipeline
The MongoDB equivalent of SQL GROUP BY + complex transforms:

```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { 
    _id: "$customer_id", 
    total_spent: { $sum: "$amount" },
    order_count: { $sum: 1 }
  }},
  { $sort: { total_spent: -1 } },
  { $limit: 10 },
  { $lookup: {                        // JOIN
    from: "customers",
    localField: "_id",
    foreignField: "_id",
    as: "customer"
  }}
]);
```

### Pipeline Stages
| Stage | SQL Equivalent | Purpose |
|-------|---------------|---------|
| `$match` | WHERE | Filter documents |
| `$project` | SELECT | Reshape documents / include/exclude fields |
| `$group` | GROUP BY | Aggregate values |
| `$sort` | ORDER BY | Sort results |
| `$limit` / `$skip` | LIMIT / OFFSET | Paginate |
| `$lookup` | LEFT JOIN | Reference documents from another collection |
| `$unwind` | — | Deconstruct array into multiple documents |
| `$facet` | — | Multi-faceted aggregation (multiple pipelines) |

## Indexing Strategy
```javascript
// Single field index
db.users.createIndex({ email: 1 });

// Compound index — order matters!
db.orders.createIndex({ status: 1, createdAt: -1 });

// Text index for full-text search
db.posts.createIndex({ title: "text", body: "text" });

// TTL index — auto-expire documents
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 86400 });

// Geospatial index
db.places.createIndex({ location: "2dsphere" });
```

### Indexing Rules of Thumb
- **ESR Rule**: Equality fields first, Sort fields second, Range fields last
- **Selectivity**: Highly selective indexes (few matching docs per key) are more efficient
- **Covered Queries**: When all required fields exist in the index (no document fetch needed)

## Scalability — Sharding & Replication

### Replication (High Availability)
- **Replica Set**: 1 Primary (writes) + N Secondaries (read replicas, failover)
- **Automatic failover**: If primary goes down, secondaries elect a new primary
- **Read Preferences**: `primary` (default), `primaryPreferred`, `secondary`, `nearest`

### Sharding (Horizontal Scaling)
```javascript
sh.shardCollection("mydb.users", { _id: "hashed" });
// Shard key determines how data is distributed across shards
```
- **Ranged sharding**: Good for range-based queries, risk of hot spots
- **Hashed sharding**: Even distribution, good for write-heavy workloads
- **Zoned sharding**: Pin data to specific shards geographically

## MongoDB vs. PostgreSQL — Decision Guide

| Factor | Choose MongoDB | Choose PostgreSQL |
|--------|---------------|-------------------|
| Schema | Flexible / evolving | Rigid / well-defined |
| Relationships | Few / contained | Complex (many JOINs) |
| Data shape | JSON-like documents | Tabular, relational |
| Consistency | Eventual (default) | Strong (ACID) |
| Transactions | Multi-document (4.0+) | Robust |
| Scale pattern | Horizontal (sharding) | Vertical + read replicas |

## Common Interview Questions

1. **"When would you use MongoDB over PostgreSQL?"** — Rapidly evolving schema, document-shaped data, horizontal scaling needs, less complex relationships.

2. **"What is the difference between SQL and NoSQL transactions?"** — MongoDB added multi-document ACID transactions in v4.0, but they're slower than PostgreSQL's due to distributed coordination. Use them sparingly.

3. **"How do you handle schema migrations in MongoDB?"** — Schema is enforced at the application level (ODM like Mongoose). Use application-level migration scripts to transform documents.

4. **"Explain the tradeoffs of embedded vs. referenced documents."** — Embedding = faster reads (one query), but 16MB limit and data duplication. Referencing = normalized, flexible, but requires `$lookup` (JOINs).

## Related Topics
- [[08_stack_deep_dives/05_databases_stack/01_sql_postgresql|PostgreSQL & SQL]]
- [[08_stack_deep_dives/05_databases_stack/03_redis_caching|Redis & Caching]]
- [[08_stack_deep_dives/05_databases_stack/index|Databases Stack Index]]
- [[01_foundations/10_sql_database_deep_dive|SQL Database Deep Dive]]

## Resources
- [MongoDB University](https://university.mongodb.com/)
- [MongoDB Docs](https://www.mongodb.com/docs/)
- [MongoDB Aggregation Pipeline](https://www.mongodb.com/docs/manual/aggregation/)