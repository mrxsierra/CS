---
type: stack
tags: [stack/databases, vector-search, rag, llm, postgresql]
created: 2026-06-30
---

# Vector Databases & pgvector: Deep-Dive Interview Guide

In the era of Generative AI and LLMs, **Vector Search** has transitioned from a niche information retrieval technique to a core architectural component (the "Long-term Memory" for RAG).

## 1. Vector Embeddings Foundations

### What are Embeddings?
- **Dense Representations:** Unlike sparse representations (TF-IDF, One-Hot), embeddings represent concepts as dense arrays of floating-point numbers (e.g., 768 or 1536 dimensions).
- **Semantic Mapping:** Words, images, or documents are mapped to a high-dimensional space where "meaningfully similar" items are located closer together.
- **Dimensional Scale:** While higher dimensions capture more nuance, they also trigger the **"Curse of Dimensionality,"** making distance calculations computationally expensive.

### Semantic Search vs. Keyword Search
- **Keyword (BM25):** Matches exact tokens. Fails on synonyms (e.g., "automobile" vs. "car").
- **Semantic (Vector):** Matches intent and context. Understands that "fast vehicle" is related to "sports car."

---

## 2. Similarity & Distance Metrics

Choosing the right metric depends entirely on how the embedding model was trained.

| Metric | Formula Logic | Best Use Case |
| :--- | :--- | :--- |
| **Cosine Similarity** | Measures the angle between two vectors. | When the **magnitude** of the vector doesn't matter (e.g., text similarity). Range: [-1, 1] or [0, 1]. |
| **L2 (Euclidean)** | Measures the straight-line distance between points. | When magnitude is important (e.g., image search, KNN). Range: [0, ∞). |
| **Inner Product** | Sum of the products of corresponding elements. | High-performance search when vectors are **normalized** (length=1), as it becomes equivalent to Cosine. |

---

## 3. Vector Indexing Algorithms

Linear search (O(N)) is impossible for millions of vectors. We use **Approximate Nearest Neighbor (ANN)** algorithms to trade a small amount of accuracy (recall) for massive speed.

### HNSW (Hierarchical Navigable Small World)
- **Concept:** A multi-layered graph structure. 
- **Navigation:** The search starts at the top layer (fewest nodes) to find the general neighborhood, then "zooms in" through lower layers to find the exact nearest neighbors.
- **Performance:** Extremely fast queries and high recall.
- **Trade-off:** High memory usage (RAM) because the graph structure is stored alongside the vectors.

### IVF (Inverted File Index)
- **Concept:** Divides the vector space into clusters (using K-Means). 
- **Search:** The query is compared against cluster centroids first, and only the vectors in the closest `nprobe` clusters are searched.
- **Trade-off:** Much lower memory footprint than HNSW, but slower query speeds.

### Quantization (Compression)
- **Product Quantization (PQ):** Breaks vectors into sub-vectors and replaces them with a "centroid ID" from a codebook. Reduces memory by 10x-100x.
- **Scalar Quantization (SQ):** Converts 32-bit floats to 8-bit integers.

---

## 4. Purpose-Built Vector Databases

| Database | Architecture Highlights | Pros/Cons |
| :--- | :--- | :--- |
| **Pinecone** | Closed-source, Managed/SaaS. | **Pros:** Zero-ops, excellent metadata filtering. **Cons:** Vendor lock-in. |
| **Qdrant** | Open-source, Rust-based. | **Pros:** High performance, native HNSW, strong filtering. **Cons:** Requires management. |
| **Milvus** | Distributed, Cloud-native. | **Pros:** Scales to billions of vectors, separates compute from storage. **Cons:** Complex to deploy. |
| **Chroma** | Simple, Python-focused. | **Pros:** Easiest for local RAG prototyping. **Cons:** Limited scaling features. |

---

## 5. Relational Integration: `pgvector`

For teams already using PostgreSQL, `pgvector` allows adding vector search without introducing a new database into the stack.

### Setup and Syntax
```sql
CREATE EXTENSION vector;

CREATE TABLE documents (
    id serial PRIMARY KEY,
    content text,
    embedding vector(1536) -- OpenAI embedding size
);

-- Search for top 5 nearest neighbors using Cosine Distance (<=>)
SELECT content FROM documents 
ORDER BY embedding <=> '[0.1, -0.2, ...]' 
LIMIT 5;
```

### Indexing in `pgvector`
- **IVFFLAT Index:** Good for large datasets where you can afford to rebuild the index occasionally.
- **HNSW Index (Added in v0.5.0):** Generally preferred for production due to better speed/recall trade-offs, though it consumes more memory.

---

## 6. Senior Technical Interview Questions

### Q1: "What is Hybrid Search, and why is it preferred over pure Vector Search for many RAG applications?"
**Answer:** Pure vector search can fail on specific tokens (product IDs, rare names, or technical jargon). **Hybrid Search** combines dense vector embeddings with sparse keyword search (BM25). 
- **Reciprocal Rank Fusion (RRF):** A common algorithm to merge the two ranked lists into a single score. 
- **Benefit:** You get the "best of both worlds"—semantic understanding from the vector side and precision for exact matches from the keyword side.

### Q2: "How do you handle the 'Metadata Filtering' problem in vector databases?"
**Answer:** There are two main strategies:
1. **Pre-filtering:** Filter metadata first, then search the vector space. (Slow if the filter is too broad).
2. **Post-filtering:** Search vectors first, then remove results that don't match metadata. (Risk of returning 0 results if the filter is too tight).
3. **Optimized Approach (Single-stage):** Modern DBs like Pinecone and Qdrant use a integrated approach where metadata indices are traversed *during* the HNSW graph traversal to ensure efficiency.

### Q3: "Explain the memory implications of scaling HNSW to 100 million vectors."
**Answer:** HNSW requires vectors to stay in RAM for low-latency search. At 1536 dimensions (float32), 100M vectors = ~600GB of raw data, plus graph overhead.
- **Solution:** Use **Product Quantization (PQ)** to compress vectors, or use a "Disk-based" ANN index (like DiskANN) which keeps only the graph in RAM and fetches vectors from SSD.

### Q4: "When should you NOT use `pgvector` and move to a dedicated Vector DB?"
**Answer:** Use `pgvector` if: You have < 1M vectors, you need ACID compliance, or you want to join vectors with existing relational data.
Move to a **Dedicated DB** if: You need to scale to 100M+ vectors, you require sub-10ms latency at massive scale, or you need complex features like multi-tenancy partitioning or serverless auto-scaling that specialized engines provide.

### Q5: "How do you evaluate the 'Quality' of a vector index?"
**Answer:** The primary metric is **Recall@K**. 
- You compare the results of the ANN index against a "Brute Force" (exact) search. 
- If Brute Force returns [A, B, C] and ANN returns [A, B, X], the Recall@3 is 66%. 
- You also measure **Latency (ms)** and **Throughput (QPS)** as you vary the index parameters (e.g., `ef_search` in HNSW).

---

## Related Topics
- [[08_stack_deep_dives/05_databases_stack/01_sql_postgresql|PostgreSQL Internals]]
- [[08_stack_deep_dives/03_data_ai_stack/05_llms_langchain|LLM & RAG Architecture]]
- [[01_foundations/10_sql_database_deep_dive|SQL Database Deep-Dive]]
- [[02_role_tracks/06_data_engineer|Data Engineer Career Track]]
