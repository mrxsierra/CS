---
type: concept
tags: [foundations, system-design, architecture, sql, ddb]
created: 2026-06-10
---

# System Design & Database Architecture

In 2026-27, "knowing a framework" is secondary to "understanding the system." This module covers the architectural judgment required to build scalable, reliable, and observable systems.

## 1. High-Level (HLD) vs. Low-Level Design (LLD)
Junior and mid-level engineers are increasingly tested on both.
- **High-Level Design (HLD)**: The "Birds-eye view." Focuses on system components, data flows, communication protocols (REST vs. gRPC), and scaling strategies (Load Balancers, Caching, Databases).
- **Low-Level Design (LLD)**: The "Micro view." Focuses on Object-Oriented Design (SOLID), Design Patterns (Factory, Strategy, Observer), class diagrams, and entity-relationship diagrams (ERDs).

## 2. Database Deep-Dive: The SQL and Database Edge
Most developers fail system integration because they cannot design a reliable schema.

### Relational Database Mechanics (RDBMS)
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability.
- **Isolation Levels**: Understanding the trade-offs between *Read Uncommitted*, *Read Committed*, *Repeatable Read*, and *Serializable*.
- **Indexing Mechanics**: 
    - **B-Trees**: Optimized for range queries and sorting (PostgreSQL/MySQL default).
    - **LSM-Trees**: Optimized for high-write throughput (NoSQL like Cassandra/LevelDB).
    - **Why too many indexes slow down writes**: Every write must update the index structure.
- **Query Optimization**: Learning to read an `EXPLAIN ANALYZE` plan to identify sequential scans vs. index scans.

### NoSQL & Distributed Storage
- **CAP Theorem & PACELC**: Choosing between Consistency and Availability during network partitions.
- **Sharding vs. Replication**: Partitioning data for scale vs. copying data for availability.

## 3. Junior System Design Blueprints
You are not expected to design AWS from scratch, but you must master these "Small App" templates:
- **API Design Standards**: Proper use of HTTP methods, semantic status codes (201 Created vs. 202 Accepted), and rate-limiting headers.
- **Cache-Aside Pattern**: Reading from cache, falling back to DB, and updating cache on miss.
- **Message Queues**: Using Kafka or RabbitMQ to decouple long-running tasks (e.g., image processing) from the request-response loop.

## 4. Core Performance Metrics
- **Latency vs. Throughput**: How fast is one request vs. how many requests can we handle per second?
- **The "Three Nines" ($99.9\%$)**: Understanding the cost and architectural complexity of high availability.
- **Horizontal vs. Vertical Scaling**: When to add a bigger machine vs. when to add more machines.

## 5. Case Study: Scalable Image Upload Service
- **Step 1: HLD**: Client -> LB -> App Server -> S3 (Storage) + RDS (Metadata).
- **Step 2: LLD**: Design a `StorageService` interface with `S3Storage` and `LocalStorage` implementations (Strategy Pattern).
- **Step 3: Verification**: How do we handle 10,000 concurrent uploads? (Async Workers + S3 Presigned URLs).

## Role-Specific Applications
- **[[02_role_tracks/02_frontend_engineer|Frontend]]**: Implementing client-side caching strategies, understanding CDN edge caching, handling optimistic UI updates.
- **[[02_role_tracks/03_backend_engineer|Backend]]**: Designing schemas, optimizing slow queries, and managing distributed state.
- **[[02_role_tracks/04_ml_engineer|ML/Data]]**: Designing feature stores and scalable model inference pipelines.
- **[[02_role_tracks/05_devops_engineer|DevOps]]**: Orchestrating containers (Kubernetes), implementing service meshes, managing CI/CD for distributed components.
- **[[02_role_tracks/06_data_engineer|Data Engineering]]**: Choosing between OLTP (Transaction) and OLAP (Analytics) databases.
- **[[02_role_tracks/07_product_manager|Product Management]]**: Understanding technical feasibility, evaluating build vs. buy decisions, estimating engineering effort.

## Related Topics
- [[01_foundations/01_dsa|DSA]]
- [[01_foundations/06_debugging_and_testing|Debugging & Testing]]
- [[01_foundations/05_networking|Networking]]
- [[02_role_tracks/01_general_swe|General SWE Track]]
