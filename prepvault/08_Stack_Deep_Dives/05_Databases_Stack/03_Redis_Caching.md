---
title: Redis & Caching Strategies
tags: ['stack/databases']
created: 2026-06-10
---

# Redis & Caching Strategies

## Overview
Redis is the industry-standard in-memory data store — used for caching, rate limiting, session storage, real-time queues, and more. In interviews, you're expected to understand its data structures, persistence tradeoffs, and distributed caching patterns.

## Redis Core Data Structures

### Strings (the simplest, but powerful)
```redis
SET user:1000:name "Alice"
GET user:1000:name           -- "Alice"
INCR page:visits             -- Atomic counter!
SETEX session:abc 3600 "data" -- Set with TTL
```

### Lists (ordered, fast push/pop at ends)
```redis
LPUSH notifications:user42 "new_message" "friend_request"
RPOP notifications:user42   -- Pop from right (FIFO)
LLEN notifications:user42   -- Length
```
**Use cases**: Message queues, activity feeds, recent actions

### Sets (unique, unordered)
```redis
SADD post:500:likes "user1" "user2" "user3"
SISMEMBER post:500:likes "user1"  -- 1 (exists)
SINTER user:1:friends user:2:friends  -- Mutual friends
```
**Use cases**: Tags, deduplication, membership checks

### Sorted Sets (unique, score-ordered)
```redis
ZADD leaderboard 100 "Alice" 85 "Bob" 200 "Charlie"
ZREVRANGE leaderboard 0 2 WITHSCORES  -- Top 3
ZINCRBY leaderboard 10 "Alice"       -- Increment score
```
**Use cases**: Leaderboards, rate limiting (sliding window), priority queues

### Hashes (grouped fields)
```redis
HSET user:1000 name "Alice" email "alice@example.com" age 30
HGETALL user:1000
HINCRBY user:1000 login_count 1
```
**Use cases**: Objects, session data, profile caching

### Bitmaps & HyperLogLog
```redis
SETBIT daily:2026-01-15 42 1  -- User 42 visited on Jan 15
GETBIT daily:2026-01-15 42    -- Did user 42 visit?
BITCOUNT daily:2026-01-15     -- Total DAU

PFADD unique:visitors "user1" "user2" "user642"
PFCOUNT unique:visitors       -- Approx 642 (HyperLogLog, ~0.81% error)
```

## Caching Patterns

### Cache-Aside (Lazy Loading)
The most common pattern:
```python
def get_user(user_id):
    # 1. Check cache
    user = redis.get(f"user:{user_id}")
    if user:
        return user
    # 2. Cache miss — query database
    user = db.query("SELECT * FROM users WHERE id = ?", user_id)
    # 3. Update cache (with TTL)
    redis.setex(f"user:{user_id}", 3600, user)
    return user
```

### Write-Through
```python
def update_user(user_id, data):
    # Write to database first
    db.execute("UPDATE users SET ... WHERE id = ?", data, user_id)
    # Update cache synchronously
    redis.setex(f"user:{user_id}", 3600, data)
```

### Write-Behind (Write-Back)
```python
def update_user(user_id, data):
    # Write to cache immediately
    redis.set(f"user:{user_id}", data)
    # Queue async write to DB
    queue.enqueue("sync_user_to_db", user_id, data)
```

## Eviction Policies
| Policy | Behavior | Use Case |
|--------|----------|----------|
| **noeviction** | Returns errors on writes when memory full | Critical data that must fit |
| **allkeys-lru** | Evicts least recently used | General purpose caching |
| **allkeys-lfu** | Evicts least frequently used | Hot-key heavy workloads |
| **volatile-lru** | Evicts LRU among keys with TTL set | Mixed cache + persistent data |
| **allkeys-random** | Random eviction | Equal-value cache entries |

## Persistence Tradeoffs

| Feature | RDB (Snapshot) | AOF (Append-Only File) |
|---------|---------------|----------------------|
| Data loss | Up to last snapshot | Up to 1 second (configurable) |
| Performance | Minimal (fork on save) | Higher write overhead |
| Recovery speed | Fast | Slow (replay all commands) |
| File size | Compact | Large (can be rewritten) |

**Best practice**: Use both — RDB for fast restores, AOF for durability. Or disable persistence entirely for pure caching use cases.

## Distributed Caching Patterns

### Rate Limiting (Sliding Window)
```redis
-- Lua script for atomic rate limiting
local key = KEYS[1]
local window = tonumber(ARGV[1])  -- 60 seconds
local max_requests = tonumber(ARGV[2])  -- 10
local now = redis.call('TIME')[1]
-- Remove old entries
redis.call('ZREMRANGEBYSCORE', key, 0, now - window)
-- Count current entries
local count = redis.call('ZCARD', key)
if count >= max_requests then
    return 0  -- Rate limited
end
redis.call('ZADD', key, now, now .. ':' .. math.random())
redis.call('EXPIRE', key, window)
return 1  -- Allowed
```

### Distributed Lock (Redlock)
```redis
SET lock:resource_id "unique_token" NX PX 30000
-- NX = only set if key doesn't exist
-- PX 30000 = 30 second TTL (safety in case holder crashes)
-- Release: if token matches, DEL lock:resource_id
```

### Cache Stampede Prevention
When a hot key expires, thousands of requests simultaneously hit the DB:
- **Mutex**: First request to detect a miss acquires a lock and regenerates cache
- **Early recomputation**: Refresh the cache before it expires (e.g., at 70% TTL)
- **Probabilistic expiration**: Randomize TTL to prevent thundering herd

## Common Interview Questions

1. **"Explain cache-aside vs. write-through with tradeoffs."** — Cache-aside: simple, handles cache failure gracefully, but initial request is slow (miss penalty). Write-through: always consistent, but slower writes, more write amplification.

2. **"How do you handle cache invalidation?"** — TTL-based expiration, event-driven invalidation (publish cache key to Redis pub/sub on data change), or write-through patterns.

3. **"What's the difference between LRU and LFU?"** — LRU evicts the least recently accessed item (good for temporal locality). LFU evicts the least frequently accessed item (good for steady-state popularity). Redis 4.0+ supports both.

4. **"How do you prevent hot keys from overwhelming a single Redis node?"** — Shard the cache by key, use client-side caching (read-through local cache), or replicate the hot key across multiple nodes.

## Related Topics
- [[08_Stack_Deep_Dives/05_Databases_Stack/01_SQL_PostgreSQL|PostgreSQL & SQL]]
- [[08_Stack_Deep_Dives/05_Databases_Stack/02_MongoDB_NoSQL|MongoDB & NoSQL]]
- [[08_Stack_Deep_Dives/05_Databases_Stack/Index|Databases Stack Index]]
- [[01_Foundations/03_System_Design|System Design]]

## Resources
- [Redis Official Docs](https://redis.io/docs/)
- [Redis University](https://university.redis.com/)
- [Martin Kleppmann's Redlock Analysis](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)