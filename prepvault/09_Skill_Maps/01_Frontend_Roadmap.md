---
title: Frontend Engineering Roadmap
tags: ['roadmap', 'visual']
---

# Frontend Engineering Roadmap

## Description
Interactive visual learning path for Frontend Engineering Roadmap.

## Visual Skill Tree (Mermaid.js)

```mermaid
graph TD

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
