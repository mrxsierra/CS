---
type: concept
tags: [stack, backend, api, rest, graphql, grpc, design]
created: 2026-06-10
---

# Backend Stack: API Design (REST, GraphQL, gRPC)

Choosing the right API style is a common System Design and Backend architecture interview topic.

---

## 1. REST (Representational State Transfer)
The most common style for web APIs. It uses standard HTTP methods and is stateless.

### Principles:
- **Resources**: Everything is a resource identified by a URI (e.g., `/users/123`).
- **Standard Methods**: GET, POST, PUT, DELETE, PATCH.
- **Statelessness**: Each request must contain all information needed to process it.
- **HATEOAS**: Providing links to other related resources in the response (rarely fully implemented).

---

## 2. GraphQL
A query language for your API, giving clients the power to ask for exactly what they need and nothing more.

### Pros:
- **No Over-fetching/Under-fetching**: Clients get exactly the fields they request.
- **Single Endpoint**: Usually `/graphql`.
- **Strongly Typed**: Schema-first development with SDL (Schema Definition Language).

### Cons:
- **Complexity**: Harder to implement server-side caching.
- **Query Complexity**: Malicious or poorly written queries can take down a server (requires depth-limiting).

---

## 3. gRPC (Google Remote Procedure Call)
A high-performance, open-source universal RPC framework.

### Characteristics:
- **Protocol Buffers**: Uses Binary serialization (Protobuf) instead of JSON.
- **HTTP/2**: Leverages multiplexing, streaming, and header compression.
- **Bidirectional Streaming**: Both client and server can send a stream of messages.
- **Best For**: Internal microservice communication where performance is critical.

---

## 4. Comparison Table

| Feature | REST | GraphQL | gRPC |
| :--- | :--- | :--- | :--- |
| **Data Format** | JSON / XML | JSON | Protobuf (Binary) |
| **Coupling** | Loose | Loose | Tight (Shared `.proto`) |
| **Efficiency** | Moderate | High (Data fetch) | Very High (Binary) |
| **Browser Support**| Native | Native (via client) | Limited (requires proxy) |

---

## 5. API Best Practices
- **Versioning**: Using URI (v1/v2) or Header-based versioning.
- **Pagination**: Using `offset/limit` or `cursor-based` (preferred for large datasets).
- **Idempotency**: Ensuring that repeating a request doesn't change the result (critical for POST/PUT).
- **Rate Limiting**: Protecting the API from abuse (Token Bucket, Leaky Bucket).

## Common Interview Questions
- **"What is the difference between PUT and PATCH?"**: PUT replaces the entire resource; PATCH applies a partial update.
- **"How do you handle breaking changes in an API?"**: Versioning, deprecation headers, and maintaining backward compatibility for a transition period.
- **"Explain Cursor-based pagination vs Offset-based."**: Offset is simple but slow for large sets and inconsistent if data is added. Cursor is faster and stable but more complex to implement.

## Related Topics
- [[01_foundations/05_networking|Networking (HTTP/2, HTTP/3)]]
- [[01_foundations/03_system_design|System Design (Load Balancing)]]
