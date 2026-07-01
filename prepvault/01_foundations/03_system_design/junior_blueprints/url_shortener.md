---
type: concept
tags: [foundations, system-design, blueprint, junior]
created: 2026-06-10
---

# System Design Blueprint: URL Shortener (e.g., Bitly)

A classic junior system design question focusing on hashing, databases, and redirection.

---

## 1. Requirements
- **Functional**:
    - Given a long URL, return a short unique alias.
    - When a user hits the short URL, redirect them to the original long URL.
- **Non-Functional**:
    - High availability (100% uptime for redirection).
    - Low latency (instant redirection).
    - Scalability (millions of URLs generated per day).

## 2. Estimations (Back-of-the-envelope)
- **Traffic**: 100M URLs per month.
- **Read/Write Ratio**: 100:1 (Redirection is much more common than creation).
- **Storage**: 100M * 500 bytes (avg URL length) = 50GB per month.

## 3. High-Level Design
`User -> Load Balancer -> App Servers -> Database / Cache`

## 4. Data Model
- **SQL (PostgreSQL)** or **NoSQL (DynamoDB/Cassandra)**.
- **Table Structure**:
    - `short_id` (PK)
    - `original_url`
    - `created_at`
    - `user_id`

## 5. The Core Logic: Generating the ID
- **Hashing (MD5/SHA256)**: Hash the URL, take the first 7 chars. (Collision risk).
- **Base62 Encoding**: Convert a numeric auto-incrementing ID to base62 (`[A-Za-z0-9]`). 
    - 6 characters = 62^6 (~56 Billion combinations).
- **Key Generation Service (KGS)**: A separate service that pre-generates unique keys and stores them in a "available" table to ensure no collisions and high speed.

## 6. Optimization: Caching
Since redirection is read-heavy, use a cache (Redis) to store the `short_id -> original_url` mapping for the most popular links (LRU policy).

---

## Role-Specific Applications
- **Backend**: API design, choosing the right hashing algorithm, handling race conditions in key assignment.
- **Frontend**: Handling HTTP 302 redirects, analytics tracking on client-side.
- **DevOps**: Scalable load balancing, managing Redis clusters for high-availability reads.
