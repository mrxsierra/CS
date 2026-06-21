---
title: Apache Spark & Big Data
tags: ['stack/data']
created: 2026-06-10
---

# Apache Spark & Big Data

## Overview
Spark is the de facto standard for distributed data processing. Data Engineering and ML interviews test your understanding of its execution model, optimization strategies, and ecosystem.

## Spark Architecture

### Driver + Executors
```
Driver (master)
├── SparkContext — connects to cluster manager
├── DAGScheduler — converts logical plan to physical stages
└── TaskScheduler — distributes tasks to executors

Executors (workers)
├── Run tasks (one thread per partition)
├── Cache data in memory
└── Return results to driver
```

### Lazy Evaluation
```python
# Nothing happens until an action is called!
df = spark.read.parquet("s3://data/events")     # Transformation
filtered = df.filter(df.revenue > 100)           # Transformation
aggregated = filtered.groupBy("region").count()  # Transformation
aggregated.show()                                # ACTION → triggers execution!
```

## RDDs, DataFrames, and Spark SQL

### RDDs (Resilient Distributed Datasets)
- Low-level API (prefer DataFrames)
- Immutable, partitioned, fault-tolerant
- Can be rebuilt from lineage if a partition fails

### DataFrames (Modern API)
```python
# DataFrames are distributed collections of rows with a schema
# Optimized by Catalyst optimizer (rule-based + cost-based)

# Reading
df = spark.read.parquet("s3://data/events/*.parquet")
df = spark.read.format("delta").load("s3://data/events/")

# Transformations
from pyspark.sql.functions import col, window, sum, avg

result = (df
    .filter(col("revenue").isNotNull())
    .withColumn("revenue_category", 
        when(col("revenue") > 1000, "high")
        .otherwise("low"))
    .groupBy(window("timestamp", "1 hour"), "region")
    .agg(
        sum("revenue").alias("total_revenue"),
        avg("revenue").alias("avg_revenue")
    )
)
```

### Spark SQL
```python
df.createOrReplaceTempView("events")
result = spark.sql("""
    SELECT 
        region,
        DATE_TRUNC('hour', timestamp) as hour,
        SUM(revenue) as total_revenue,
        COUNT(DISTINCT user_id) as unique_users
    FROM events
    WHERE revenue IS NOT NULL
    GROUP BY region, DATE_TRUNC('hour', timestamp)
    HAVING total_revenue > 1000
    ORDER BY total_revenue DESC
""")
```

## Performance Optimization

### Shuffling — The #1 Performance Killer
Shuffling moves data between executors over the network. It's triggered by:
- `groupBy()`, `join()`, `reduceByKey()`, `repartition()`
- **Minimizing shuffle**: 
  - Use `reduceByKey` instead of `groupByKey` (combines before shuffle)
  - Broadcast small tables instead of shuffling large joins
  - Partition data by join key before writing

### Broadcast Join
```python
# Small table (< 100MB) → broadcast to all executors, no shuffle!
small_df = spark.read.parquet("s3://data/countries/")
result = large_df.join(broadcast(small_df), "country_code")
```

### Partitioning
```python
# Good partitioning = optimal parallelism
df.repartition(200, "date")          # Explicit repartition (triggers shuffle)
df.coalesce(50)                      # Reduce partitions (no shuffle)
df.write.partitionBy("date", "region").parquet("s3://data/out/")
```

### Avoiding Skew
When one partition has much more data than others:
```python
# Salting — add random prefix to skewed keys
from pyspark.sql.functions import rand, concat, lit

# Add salt to skewed key, join, then remove salt
salted_df = skewed_df.withColumn("salt", (rand() * 10).cast("int"))
salted_df = salted_df.withColumn("salted_key", concat(col("key"), lit("_"), col("salt")))
```

## The Spark Ecosystem

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **Spark SQL** | SQL on DataFrames | Analysts, quick queries |
| **Spark Streaming** | Micro-batch streaming | Near-real-time processing (latency > 1s) |
| **MLlib** | Distributed ML | Large-scale model training |
| **GraphX** | Graph processing | PageRank, connected components |
| **Delta Lake** | ACID transactions on data lakes | Reliable data pipelines |
| **Apache Iceberg** | Table format for large datasets | Open-source, wide engine support |

## Common Interview Questions

1. **"Explain lazy evaluation in Spark."** — Transformations (map, filter, groupBy) build a DAG but don't execute. Only actions (count, show, save) trigger execution. This allows the Catalyst optimizer to combine/reorder operations for maximum efficiency.

2. **"What is a shuffle and why is it expensive?"** — A shuffle redistributes data across partitions, requiring network I/O, serialization, and disk writes. It's the most expensive operation in Spark. Always try to minimize it.

3. **"What's the difference between `groupByKey` and `reduceByKey`?"** — `groupByKey` sends all values to a single partition (heavy shuffle + memory). `reduceByKey` combines values locally before shuffling (map-side combine → less data shuffled).

4. **"How does the Catalyst optimizer work?"** — Catalyst applies rule-based (predicate pushdown, projection pruning) and cost-based optimizations (choosing join strategies) to your logical plan before execution.

## Related Topics
- [[08_Stack_Deep_Dives/03_Data_AI_Stack/01_Python_Data_Analytics|Python for Data Analytics]]
- [[08_Stack_Deep_Dives/03_Data_AI_Stack/06_MLflow_Deployment|MLOps & Model Deployment]]
- [[08_Stack_Deep_Dives/03_Data_AI_Stack/Index|Data & AI Stack Index]]
- [[02_Role_Tracks/06_Data_Engineer|Data Engineering Track]]

## Resources
- [Spark Official Docs](https://spark.apache.org/docs/latest/)
- [Learning Spark (O'Reilly)](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/)
- [High Performance Spark (O'Reilly)](https://www.oreilly.com/library/view/high-performance-spark/9781491943199/)
- [Delta Lake Docs](https://delta.io/)