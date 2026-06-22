---
title: Backend Engineering Roadmap
tags: ['roadmap', 'visual']
---

# Backend Engineering Roadmap

## Description
Interactive visual learning path for Backend Engineering Roadmap.

## Visual Skill Tree (Mermaid.js)

```mermaid
graph TD

    subgraph "Phase 1: Core Fundamentals"
        A[Pick a Language: Python/Node/Go/Rust 💻]:::foundations
        B[OS Basics: Processes & Memory 🧠]:::foundations
        C[Linux & Shell Scripting 🐚]:::foundations
        A --> B --> C
    end

    subgraph "Phase 2: Networking & APIs"
        D[Networking: TCP/IP, HTTP/S 🌐]:::tooling
        E[API Design: REST, GraphQL, gRPC 🔌]:::tooling
        F[Auth: JWT, OAuth2, OpenID 🔐]:::tooling
        C --> D --> E --> F
    end

    subgraph "Phase 3: Data Persistence"
        G[Relational: PostgreSQL 🐘]:::frameworks
        H[NoSQL: MongoDB/Redis 🍃]:::frameworks
        I[Database Internals: Indexing, ACID ⚙️]:::frameworks
        F --> G
        G --> H --> I
    end

    subgraph "Phase 4: Distributed Systems"
        J[Microservices & Event-Driven 🏗️]:::advanced
        K[Message Queues: Kafka/RabbitMQ 📩]:::advanced
        L[System Design Patterns 🏛️]:::advanced
        I --> J --> K --> L
    end

    subgraph "Phase 5: Cloud & Scalability"
        M[Docker & Containerization 🐳]:::cloud
        N[CI/CD Pipelines 🔄]:::cloud
        O[Observability: ELK/Prometheus 📈]:::cloud
        L --> M --> N --> O
    end


    classDef foundations fill:#f9f,stroke:#333,stroke-width:2px;
    classDef tooling fill:#bbf,stroke:#333,stroke-width:2px;
    classDef frameworks fill:#bfb,stroke:#333,stroke-width:2px;
    classDef advanced fill:#fdb,stroke:#333,stroke-width:2px;
    classDef specialized fill:#dfd,stroke:#333,stroke-width:2px;
    classDef cloud fill:#bff,stroke:#333,stroke-width:2px;
    classDef security fill:#fbb,stroke:#333,stroke-width:2px;

```

## Related Topics
- [[00_Getting_Started|Back to Home]]
- [[Index|All Skill Maps]]
