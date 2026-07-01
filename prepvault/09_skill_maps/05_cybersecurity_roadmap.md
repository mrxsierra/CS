---
title: Cybersecurity Roadmap
tags: ['roadmap', 'visual']
---

# Cybersecurity Roadmap

## Description
Interactive visual learning path for Cybersecurity Roadmap.

## Visual Skill Tree (Mermaid.js)

```mermaid
graph TD

    subgraph "Phase 1: Foundations"
        A[Networking: TCP/IP & OSI 🌐]:::foundations
        B[OS Internals & Hardening 🛡️]:::foundations
        C[Security Fundamentals: CIA 🔒]:::foundations
        A --> B --> C
    end

    subgraph "Phase 2: Security Engineering"
        D[Cryptography & PKI 🔑]:::tooling
        E[Identity & Access (IAM) 🆔]:::tooling
        F[Network Sec: WAF/Firewalls 🧱]:::tooling
        C --> D --> E --> F
    end

    subgraph "Phase 3: Blue Team (Defensive)"
        G[SIEM & SOC Operations 🕵️]:::frameworks
        H[Incident Response 🚑]:::frameworks
        I[Digital Forensics 🔎]:::frameworks
        F --> G --> H --> I
    end

    subgraph "Phase 4: Red Team (Offensive)"
        J[Ethical Hacking & Pentesting ⚔️]:::advanced
        K[Web App Sec: OWASP Top 10 🕸️]:::advanced
        L[Exploit Development 💥]:::advanced
        F --> J --> K --> L
    end

    subgraph "Phase 5: GRC & Cloud Sec"
        M[Governance, Risk, Compliance 📜]:::security
        N[Cloud Security (AWS/Azure) ☁️]:::security
        O[DevSecOps Integration 🔄]:::security
        I --> M
        L --> N
        M --> O
        N --> O
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
