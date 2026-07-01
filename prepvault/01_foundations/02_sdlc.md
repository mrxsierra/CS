---
type: concept
tags: [foundations, sdlc, git, devops]
created: 2026-06-10
---

# SDLC, Git Architecture & DevOps Mastery

Modern software development has shifted from "writing code" to "owning systems." This module covers the collaborative workflows and automated pipelines required for 2026-27 engineering.

## 1. Professional Git Architecture
If you only know `git add` and `git commit`, you are a liability. Enterprise teams require advanced version control proficiency.

### Collaborative Workflows
- **Trunk-Based Development**: The industry standard for high-velocity teams. Developers merge short-lived feature branches into `main` multiple times a day. This minimizes "merge hell" and enables true CI/CD.
- **GitFlow**: A legacy, more structured branching model (Master, Develop, Feature, Release, Hotfix). Useful for teams with strict, scheduled release cycles (e.g., embedded systems).

### Advanced Git Techniques
- **Interactive Rebase (`git rebase -i`)**: Used to clean up commit history before pushing. You should "squash" messy "fixup" commits into logical, readable units.
- **Git Hooks**: Use tools like **Husky** or **pre-commit** to automate linting, type-checking, and unit tests *locally* before code ever reaches the remote repository.
- **Merge Conflict Resolution**: Learn to resolve conflicts by understanding the context of both changes, rather than just choosing "ours" or "theirs."

## 2. Modern CI/CD Pipelines
The goal of a pipeline is to reduce the risk of deployment through automated verification.

### The Pipeline Flow
1. **Lint**: Check for style and syntax errors.
2. **Type-Check**: (For TS/Go/Java) Ensure type safety.
3. **Unit Test**: Verify individual logic components.
4. **Build**: Package the application (e.g., Docker image).
5. **Stage**: Deploy to a production-like environment.
6. **Integration/E2E Tests**: Verify the system works as a whole.
7. **Deploy**: Move to production.

### Deployment Strategies
- **Canary Releases**: Deploying the new version to a small subset of users (e.g., $5\%$) to monitor for errors before a full rollout.
- **Blue-Green Deployment**: Maintaining two identical production environments. Switch traffic from Blue (old) to Green (new) instantaneously.

## 3. Agile & Scrum Ceremonies
Agile is about feedback loops, not just "going fast."
- **Daily Standup**: "What did I do? What will I do? Am I blocked?"
- **Sprint Planning**: Negotiating the "Sprint Goal" and selecting items from the backlog.
- **Backlog Grooming**: Breaking down complex features into "User Stories" and estimating effort (Story Points).
- **PR Review**: Not just a "LGTM" (Looks Good To Me). Check for performance, security, and edge cases.

## 4. Test-Driven Development (TDD)
Writing tests before code ensures your requirements are clear and your code is verifiable from day one.
- **Red**: Write a failing test.
- **Green**: Write the minimal code to pass the test.
- **Refactor**: Clean up the code while keeping the test green.

## Role-Specific Applications
- **[[02_role_tracks/02_frontend_engineer|Frontend]]**: Managing UI regression tests, versioning CSS systems, and automating Vercel/Netlify deployments.
- **[[02_role_tracks/03_backend_engineer|Backend]]**: Automating database migrations, managing API versioning, and implementing load tests in CI.
- **[[02_role_tracks/04_ml_engineer|ML / Data Science]]**: MLOps — versioning data and models, monitoring model performance in production, implementing automated data validation.
- **[[02_role_tracks/05_devops_engineer|DevOps]]**: Orchestrating the entire pipeline via Jenkins, GitHub Actions, or GitLab CI.
- **[[02_role_tracks/06_data_engineer|Data Engineering]]**: Managing data pipeline lifecycles, versioning ETL code, orchestrating workflow DAGs.
- **[[02_role_tracks/07_product_manager|Product Management]]**: Defining product roadmaps, prioritizing backlog, managing stakeholder expectations through agile ceremonies.

## Related Topics
- [[01_foundations/06_debugging_and_testing|Debugging & Testing]]
- [[01_foundations/03_system_design|System Design]]
- [[02_role_tracks/01_general_swe|General SWE Track]]
