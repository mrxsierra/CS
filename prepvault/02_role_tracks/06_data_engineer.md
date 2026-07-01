---
type: role
tags: [role/data-eng, track]
created: 2024-06-10
---

# Data Engineer Interview Track

## 1. Role Overview
Data Engineering is the discipline of building systems that collect, transform, and store data for analytical or operational use. If Data Science is about "finding insights," Data Engineering is about building the "plumbing" that makes those insights possible. In the modern era, this involves handling massive scale, real-time streaming, and high reliability.

### The Interview Philosophy
Data Engineering interviews test a hybrid of backend engineering and data-specific knowledge:
-   **Data Manipulation:** Can you transform messy, unstructured datasets into clean, structured tables using SQL or Python?
-   **Scalability:** How do you process a petabyte of data without crashing the cluster or overspending?
-   **Storage Tradeoffs:** When do you use a Data Lake, a Data Warehouse, or a modern Lakehouse?
-   **SQL Mastery:** Can you write complex, performant queries that run efficiently on billion-row tables?

### Typical Interview Stages
1.  **SQL Deep Dive (45-60 min):** Solving complex analytical problems using Window Functions, Joins, Aggregations, and CTEs.
2.  **Data Coding (Python/Scala/Java):** Implementing data processing logic (e.g., "Build a group-by aggregator from scratch" or "Parse this custom JSON format").
3.  **Data System Design:** Designing an end-to-end data platform (e.g., "Design a real-time analytics system for a ride-sharing app").
4.  **Schema & Data Modeling:** Modeling a business domain (e.g., "Design the data warehouse schema for an E-commerce company").
5.  **Big Data Internals:** Questions about how Spark (Shuffling, DAGs, Caching), Kafka (Partitioning, Replication, Offsets), or Snowflake work under the hood.

---

## 2. Foundational Prerequisites
Success in Data Engineering requires a solid technical foundation:

-   **[[01_foundations/03_system_design|System Design]]:** Specifically focused on high-throughput data ingestion, storage, and distributed processing. Understand CAP Theorem and PACELC.
-   **[[01_foundations/01_dsa|DSA]]:** Focus on HashMaps, Sorting algorithms, and Trees. Understanding the cost of data movement and Big-O in the context of data processing.
-   **Databases:** Deep understanding of SQL, NoSQL (Columnar vs. Row vs. Key-Value), and ACID vs. BASE properties.
-   **[[01_foundations/04_operating_systems|Operating Systems]]:** Understanding File Systems (HDFS, S3), I/O wait, CPU scheduling, and Memory management (Garbage Collection in JVM-based systems like Spark).
-   **[[01_foundations/05_networking|Networking]]:** Understanding data transfer protocols, handling API rate limits, optimizing network throughput for large-scale data movement.
-   **[[01_foundations/02_sdlc|SDLC]]:** Managing data pipeline lifecycles, versioning ETL code, orchestrating workflow DAGs with Airflow.

---

## 3. 2026-27 Ecosystem Focus: Data Lakehouses
The focus is on building robust, clean pipelines for unstructured data:
- **Data Lakehouse Architecture**: Combining Data Lakes (S3) with Warehouse features (Snowflake/Databricks).
- **Streaming & Real-time**: Ingesting data via Kafka and processing with Flink/Spark Streaming.
- **Data Quality & Governance**: Using dbt and Great Expectations to ensure pipeline integrity.

## 4. 12-Week Learning Pathway
- **Week 1-3: SQL & Relational Warehousing**: Analytic window functions, query tuning, and Star/Snowflake schemas.
- **Week 4-7: Big Data & Batch Pipelines**: Distributed processing with Spark, transformations with dbt.
- **Week 8-12: Orchestration & Stream Processing**: Airflow DAGs, Kafka brokers, and stream ingestion.

## 5. Core Competencies

### A. SQL Mastery (The Non-Negotiable)
You must be an expert in SQL.
-   **Window Functions:** `RANK()`, `DENSE_RANK()`, `LEAD()`, `LAG()`, `OVER(PARTITION BY ...)`.
-   **Complex Joins:** Self-joins, Cross-joins, and understanding Join algorithms (Hash Join, Sort-Merge Join, Nested Loop).
-   **Performance Tuning:** Understanding `EXPLAIN` plans, Indexing (B-Tree, Bitmap, GIN), Partitioning, and Bucketing.
-   **CTEs vs. Subqueries:** Writing readable and maintainable SQL for complex multi-step transformations.

### B. Big Data Frameworks (Spark Focus)
-   **Apache Spark Internals:** 
    -   **Shuffling:** The process of moving data between nodes. It's the #1 performance killer.
    -   **Partitioning:** How to split data to avoid "Data Skew."
    -   **Broadcast Joins:** Joining a small table with a large one by sending the small table to all nodes.
    -   **Lazy Evaluation:** Code is only executed when an "Action" is called (e.g., `count`, `collect`, `save`).
-   **Orchestration:** Managing dependencies using Apache Airflow (DAGs), Dagster, or Prefect.

### C. Data Warehousing & Lakehouses
-   **Cloud Data Warehouses:** Snowflake, BigQuery, Redshift. Separation of storage and compute.
-   **Data Lakehouse:** Modern architecture that brings ACID transactions and schema enforcement to Data Lakes.
    -   **Formats:** Apache Iceberg, Apache Hudi, Delta Lake.
-   **OLAP vs. OLTP:** Knowing when to use a row-oriented database (for transactions) vs. column-oriented (for analytics).

---

## 4. Role-Specific Deep Dives

### Deep Dive 1: Data Modeling (The "Medallion" Architecture)
A common pattern in modern Data Engineering:
-   **Bronze (Raw):** Landing zone for raw data. Minimal transformations.
-   **Silver (Cleansed/Curated):** Data is filtered, cleansed, and joined. Represents the "Source of Truth."
-   **Gold (Aggregated/Business):** Data is aggregated for specific business use cases (e.g., a "Daily Active Users" table).

### Deep Dive 2: Batch vs. Stream Processing
**Batch (Spark, MapReduce):**
-   Processing data in large chunks at scheduled intervals.
-   Good for historical analysis and complex joins.
**Streaming (Flink, Kafka Streams, Spark Streaming):**
-   Processing data event-by-event in real-time.
-   **Concepts:** 
    -   **Windowing:** Tumbling (fixed size), Sliding (overlapping), Session (activity-based).
    -   **Watermarks:** How the system handles late-arriving data.
    -   **Exactly-once semantics:** Ensuring data isn't duplicated during failures.

### Deep Dive 3: Change Data Capture (CDC)
**Problem:** How to sync a production DB to a Data Warehouse in real-time.
-   **Log-based CDC:** Reading the database's transaction log (e.g., MySQL Binlog or Postgres WAL).
-   **Flow:** DB -> Debezium -> Kafka -> Flink/Spark -> Snowflake.
-   *Benefit:* Extremely low impact on the source system's performance.

### Deep Dive 4: Data Quality, Reliability, and Mesh
-   **Validation:** Using frameworks like **Great Expectations** or **dbt tests** to ensure data meets business rules (e.g., "column X must never be null"). Implementing "Data Contracts" to prevent breaking upstream changes.
-   **Data Observability:** Monitoring for "Data Downtime" — when data is missing, late, or wrong. Using tools like Monte Carlo or Bigeye to detect anomalies in data volume or distribution.
-   **Data Mesh:** A decentralized architectural pattern where data is treated as a product and owned by the domain teams that produce it. Moving away from the "Centralized Data Team" bottleneck to a self-service model.
-   **Data Lineage**: Tracking the flow of data from source to consumption. Essential for debugging and regulatory compliance (GDPR/HIPAA).

### Deep Dive 5: Modern Data Stack (MDS) & dbt
The "Analytics Engineer" workflow:
- **dbt (data build tool)**: Transforming data using SQL and Jinja. Version controlling your transformations and automating documentation/testing.
- **ELT vs. ETL**: Why modern warehouses prefer loading raw data first (ELT) and then transforming it using their own elastic compute (Snowflake/BigQuery).
- **Data Governance**: Managing metadata, access control, and classification of sensitive data across the entire data lifecycle.
- **Reverse ETL**: Syncing processed data from the warehouse back into operational tools (e.g., Salesforce, Zendesk) for business use.

### Deep Dive 6: Advanced Data Modeling
- **The Data Vault**: A modeling technique designed for long-term historical storage and scalability.
- **Dimensional Modeling (Kimball)**: Focus on Facts and Dimensions for ease of use by analysts.
- **One Big Table (OBT)**: When to denormalize everything for ultra-fast query performance in modern columnar warehouses.

### Deep Dive 7: Data Governance, Privacy, and Ethics
In 2026-27, a Data Engineer must be a guardian of data integrity and privacy.
- **GDPR & HIPAA Compliance**: Implementing "Right to be Forgotten" (User deletion) and PII masking at the pipeline level.
- **Access Control (RBAC/ABAC)**: Using tools like Apache Ranger or Immuta to manage fine-grained access to sensitive tables.
- **Data Auditing**: Maintaining a trail of who accessed what data and when.
- **Ethical AI Data**: Ensuring the datasets provided to ML models are representative and free from sampling bias.

---

## 5. Big Data Performance Tuning
Beyond simple query optimization.
- **Data Skew**: Identifying and fixing skewed partitions using salting or specialized join strategies.
- **Small File Problem**: How to compact millions of tiny files in a Data Lake to avoid metadata overhead.
- **Vectorized Execution**: How modern engines (Trino, DuckDB) process batches of rows simultaneously using SIMD instructions.

---

## 6. Common Interview Questions & Detailed Walkthroughs

### SQL Scenario: "The Consecutive Login Problem"
**Problem:** Find all users who logged in for 3 or more consecutive days.
**Solution:**
1.  Assign a `ROW_NUMBER()` to each login for each user, ordered by date.
2.  Subtract the row number (as days) from the login date.
3.  If the resulting date (the "Anchor Date") is the same for multiple logins, they are consecutive.
4.  Group by `user_id` and `anchor_date`, then `COUNT(*) >= 3`.

### SQL Scenario: "User Retention Cohorts"
**Problem**: Calculate the percentage of users who returned to the app 7 days after their first signup, grouped by signup month.
**Solution**:
1. **Find Signups**: Create a CTE to find the `signup_date` for each user.
2. **Find Activity**: Join the signup CTE with the `activity_logs` table where `activity_date = signup_date + 7`.
3. **Aggregate**: Group by `signup_month` and calculate `COUNT(retained_users) / COUNT(signed_up_users)`.

### Data System Design: "Real-time Ad Click Aggregator"
1.  **Ingestion:** Kafka to handle high-volume event streams (100k+ events/sec) with multiple partitions for parallelism.
2.  **Processing:** Apache Flink to aggregate clicks over a 1-minute tumbling window. Handle late data with a 5-second watermark to ensure accuracy.
3.  **Storage:** Store aggregated results in a specialized OLAP store like Druid, ClickHouse, or Pinot for sub-second query performance on dashboards.
4.  **Fault Tolerance:** Use Flink's checkpointing (Stateful functions) to ensure "Exactly-Once" processing semantics.

### Practical Challenge: "Handling Data Backfills"
**Problem**: You need to re-process 2 years of data because a bug was found in the transformation logic.
**Solution**:
1. **Idempotency**: Ensure your pipeline can be re-run for any date range without creating duplicate records.
2. **Partition Overwrite**: Use Spark's dynamic partition overwrite to replace only the affected dates in S3/HDFS.
3. **Resource Scaling**: Spin up a temporary, larger cluster to handle the massive backlog in a short time.

### Practical Challenge: "Data Skew in Spark"
**Problem:** Your Spark job is slow because one task is taking 90% of the time while others are idle.
**Solution:**
-   **Salting:** Add a random "salt" (e.g., a number from 0-9) to the join key to redistribute the data.
-   **Broadcast Join:** If one table is small enough to fit in memory, broadcast it.
-   **Filtering:** Often skew is caused by a large number of NULL or "default" keys. Filter these out if possible.

---

## 6. Data Engineering Glossary
-   **ETL (Extract, Transform, Load):** The traditional data integration process.
-   **ELT:** Transforming data *inside* the data warehouse (modern cloud approach).
-   **Parquet:** A columnar storage format optimized for analytical queries.
-   **Avro:** A row-based format optimized for write-heavy streaming.
-   **Data Skew:** When data is not evenly distributed across a cluster, causing bottlenecks.
-   **DAG (Directed Acyclic Graph):** A collection of tasks with dependencies, used by Airflow and Spark.
-   **HDFS (Hadoop Distributed File System):** A distributed file system that provides high-throughput access to application data.

---

## 7. Company-Specific Patterns

### Meta (Facebook)
-   **Focus:** Heavy on SQL and "Product Sense." Be ready to define metrics for Facebook/Instagram features and design the pipelines to calculate them.
-   **Tip:** Master Spark and Presto/Trino internals. Understand the difference between internal data warehouses like "Hive" and "Presto."

### Amazon
-   **Focus:** Scale and cost-efficiency. Deep knowledge of AWS services (S3, Redshift, Glue, Athena, Kinesis).
-   **Tip:** Understand the cost tradeoffs between different storage tiers and compute engines.

### Google (GCP)
-   **Focus:** BigQuery, Dataflow (Apache Beam), and Pub/Sub.
-   **Tip:** Understand the "Dataflow Model" (What, Where, When, How) for stream processing.

---

## 8. Detailed Roadmap: How to Prepare
1.  **Phase 1 (Weeks 1-2):** Master Advanced SQL. Solve "Hard" problems on LeetCode/StrataScratch. Focus on window functions and complex joins.
2.  **Phase 2 (Weeks 3-5):** Learn Python/Scala for data processing. Build a small end-to-end ETL pipeline (e.g., Scraping data -> S3 -> Spark -> Redshift).
3.  **Phase 3 (Weeks 6-8):** Deep dive into Spark and Kafka. Understand distributed computing concepts like shuffling, partitioning, and replication.
4.  **Phase 4 (Weeks 9-10):** Practice Data Modeling and System Design. Focus on the "Tradeoffs" (e.g., latency vs. cost vs. accuracy).
5.  **Phase 5 (Mocks):** Practice explaining your data architecture and how you handle failures (retries, idempotency, monitoring).

## Related Topics
-   [[01_foundations/03_system_design|Distributed Systems and Databases]]
-   [[02_role_tracks/03_backend_engineer|Backend for Data Engineers]]
-   [[03_interview_formats/02_system_design_rounds|Data System Design Rounds]]
