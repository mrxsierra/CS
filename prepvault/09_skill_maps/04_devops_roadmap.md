---
title: DevOps & Cloud Roadmap
tags: ['roadmap', 'visual']
---

# DevOps & Cloud Roadmap

## Description
Interactive visual learning path for DevOps & Cloud Roadmap.

## Visual Skill Tree (Mermaid.js)

```mermaid
graph TD

    subgraph "Phase 1: Admin & Scripting"
        A[Linux SysAdmin & Bash 🐧]:::foundations
        B[Networking & Security 🌐]:::foundations
        C[Git & Collaborative Workflows 🤝]:::foundations
        A --> B --> C
    end

    subgraph "Phase 2: Infrastructure as Code"
        D[Configuration: Ansible 🛠️]:::tooling
        E[Provisioning: Terraform 🏗️]:::tooling
        F[Cloud: AWS/Azure/GCP ☁️]:::tooling
        C --> D --> E --> F
    end

    subgraph "Phase 3: Containers"
        G[Docker Mastery 🐳]:::frameworks
        H[Kubernetes Foundations ☸️]:::frameworks
        I[Helm & GitOps ⚓]:::frameworks
        F --> G --> H --> I
    end

    subgraph "Phase 4: CI/CD Mastery"
        J[GitHub Actions/Jenkins 🔄]:::advanced
        K[Artifacts & Registry 📦]:::advanced
        L[Deployment: Canary/Blue-Green 🚀]:::advanced
        I --> J --> K --> L
    end

    subgraph "Phase 5: Reliability & Monitoring"
        M[Prometheus & Grafana 📊]:::cloud
        N[Logging: ELK/Loki 📝]:::cloud
        O[SRE Principles & SLIs/SLOs ⚖️]:::cloud
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
- [[00_getting_started|Back to Home]]
- [[index|All Skill Maps]]
