import os

base_dir = "/home/team/shared/prepvault/09_Skill_Maps"

# Shared styles
STYLES = """
    classDef foundations fill:#f9f,stroke:#333,stroke-width:2px;
    classDef tooling fill:#bbf,stroke:#333,stroke-width:2px;
    classDef frameworks fill:#bfb,stroke:#333,stroke-width:2px;
    classDef advanced fill:#fdb,stroke:#333,stroke-width:2px;
    classDef specialized fill:#dfd,stroke:#333,stroke-width:2px;
    classDef cloud fill:#bff,stroke:#333,stroke-width:2px;
    classDef security fill:#fbb,stroke:#333,stroke-width:2px;
"""

def update_roadmap(filename, title, mermaid_content):
    filepath = os.path.join(base_dir, filename)
    content = f"""---
title: {title}
tags: ['roadmap', 'visual']
---

# {title}

## Description
Interactive visual learning path for {title}.

## Visual Skill Tree (Mermaid.js)

```mermaid
graph TD
{mermaid_content}
{STYLES}
```

## Related Topics
- [[00_Getting_Started|Back to Home]]
- [[Index|All Skill Maps]]
"""
    with open(filepath, 'w') as f:
        f.write(content)

# 1. Frontend
frontend_mermaid = """
    subgraph "Phase 1: Foundations"
        A[HTML5 & Semantic Tags 🏗️]:::foundations
        B[CSS3: Flex, Grid, Responsive 🎨]:::foundations
        C[JavaScript ES6+: DOM, Fetch, Async ⚡]:::foundations
        A --> B --> C
    end

    subgraph "Phase 2: Modern Tooling"
        D[Git & GitHub 🤝]:::tooling
        E[Package Managers: npm/pnpm 📦]:::tooling
        F[Vite & Build Tools 🚀]:::tooling
        C --> D --> E --> F
    end

    subgraph "Phase 3: Framework Mastery"
        G[React.js: Hooks & Context ⚛️]:::frameworks
        H[State Management: Zustand/Redux 🧠]:::frameworks
        I[Styling: Tailwind CSS 💅]:::frameworks
        F --> G
        G --> H
        G --> I
    end

    subgraph "Phase 4: Advanced Architecture"
        J[Next.js: App Router, SSR, ISR 🌐]:::advanced
        K[TypeScript Mastery 🛡️]:::advanced
        L[Testing: Vitest, Playwright 🧪]:::advanced
        H --> J
        I --> J
        J --> K --> L
    end

    subgraph "Phase 5: Specialized Tracks"
        M[Performance Optimization ⏱️]:::specialized
        N[Accessibility - a11y ♿]:::specialized
        O[Design Systems 📐]:::specialized
        L --> M
        L --> N
        L --> O
    end
"""

# 2. Backend
backend_mermaid = """
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
"""

# 3. Data & AI
data_ai_mermaid = """
    subgraph "Phase 1: Foundations"
        A[Python for Data 🐍]:::foundations
        B[SQL & Database Mastery 📊]:::foundations
        C[Math: Stats & Linear Algebra 📐]:::foundations
        A --> B --> C
    end

    subgraph "Phase 2: Data Engineering"
        D[ETL Pipelines: Airflow 🚜]:::tooling
        E[Big Data: Spark/Hadoop 🐘]:::tooling
        F[Data Warehousing: Snowflake ❄️]:::tooling
        C --> D --> E --> F
    end

    subgraph "Phase 3: Data Science"
        G[Analysis: Pandas/NumPy 🐼]:::frameworks
        H[Viz: Tableau/Seaborn 📈]:::frameworks
        I[Exploratory Data Analysis 🔍]:::frameworks
        C --> G --> H --> I
    end

    subgraph "Phase 4: Machine Learning"
        J[Classical ML: Scikit-learn 🤖]:::advanced
        K[Deep Learning: PyTorch/TF 🧠]:::advanced
        L[MLOps: MLflow/DVC 🔄]:::advanced
        I --> J --> K --> L
    end

    subgraph "Phase 5: Generative AI"
        M[LLM Foundations: Transformers Transformers 🎭]:::specialized
        N[RAG Architecture 📚]:::specialized
        O[Agentic Workflows 🤖]:::specialized
        L --> M --> N --> O
    end
"""

# 4. DevOps
devops_mermaid = """
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
"""

# 5. Cybersecurity
cyber_mermaid = """
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
"""

update_roadmap("01_Frontend_Roadmap.md", "Frontend Engineering Roadmap", frontend_mermaid)
update_roadmap("02_Backend_Roadmap.md", "Backend Engineering Roadmap", backend_mermaid)
update_roadmap("03_Data_AI_Roadmap.md", "Data & AI Roadmap", data_ai_mermaid)
update_roadmap("04_DevOps_Roadmap.md", "DevOps & Cloud Roadmap", devops_mermaid)
update_roadmap("05_Cybersecurity_Roadmap.md", "Cybersecurity Roadmap", cyber_mermaid)

print("Beautiful roadmaps generated!")
