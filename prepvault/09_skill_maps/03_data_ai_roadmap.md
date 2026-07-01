---
title: Data & AI Roadmap
tags: ['roadmap', 'visual']
---

# Data & AI Roadmap

## Description
Interactive visual learning path for Data & AI Roadmap.

## Visual Skill Tree (Mermaid.js)

```mermaid
graph TD

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
