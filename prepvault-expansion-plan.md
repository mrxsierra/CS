# PrepVault Expansion Plan (Phase 2)

## Overview
This document outlines the structural expansion of the PrepVault Obsidian vault to accommodate specialized technical roles and stack-specific mastery modules, reflecting the 2026-27 tech recruitment market.

## 1. Language Internals Expansion
- **Rust.md**: Added to `01_Foundations/07_Language_Internals/`. Focuses on Ownership, Borrowing, Lifetimes, and the Send/Sync traits.
- **Goal**: Provide a deep-dive alternative to C++/Go for systems engineering roles.

## 2. New Role Tracks
- **09_Data_Scientist.md**: Focuses on the DS interview loop, statistics, ML theory, and A/B testing.
- **10_Data_Analyst.md**: Emphasizes SQL mastery, BI tools, and data storytelling.
- **Linking**: These roles link back to `09_SQL_Database_Deep_Dive` and `12_AI_Orchestration`.

## 3. Stack Deep Dives Module (`08_Stack_Deep_Dives/`)
A new directory structure for framework-specific knowledge:
- **Frontend**: React, Next.js, Vite, HTML/CSS.
- **Backend**: Node.js, FastAPI, Django/Flask, Rust Systems, API Design.
- **Data & AI**: Python Analytics/DS, ML Mastery, Deep Learning, LLMs/LangChain, MLOps, Spark.
- **DevOps & Cloud**: Docker, Kubernetes, Terraform, GitHub Actions.
- **Databases**: PostgreSQL, MongoDB, Redis.

## 4. Skill Maps (`09_Skill_Maps/`)
Visual-ready roadmaps for each major track:
- Frontend, Backend, Data & AI, DevOps, Cybersecurity.
- These roadmaps will use Mermaid diagrams (to be added by writers) to show prerequisite paths.

## 5. Next Steps for Content Writers
1. **Populate Stubs**: Writers should use the `concept_template` or `role_template` to fill in the technical details for each new file.
2. **Interlinking**: Ensure Stack Deep Dives link back to the relevant Foundations (e.g., React links to JS Internals).
3. **Proof of Work**: Add sample project ideas to each Role Track using the `proof_of_work_template`.

## Navigation Updates
- `00_Getting_Started.md` has been updated to include these new sections.
- `06_Tag_Index.md` now includes Dataview queries for `#stack/data` and `#roadmap`.
