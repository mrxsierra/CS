---
type: concept
tags: [stack, devops, github-actions, ci-cd, automation, workflow]
created: 2026-06-10
---

# DevOps Stack: GitHub Actions & CI/CD

GitHub Actions makes it easy to automate all your software workflows, now with world-class CI/CD. Build, test, and deploy your code right from GitHub.

---

## 1. Core Concepts
- **Workflow**: An automated process that you add to your repository. Workflows are made up of one or more jobs and can be scheduled or triggered by an event.
- **Event**: A specific activity in a repository that triggers a workflow (e.g., `push`, `pull_request`, `release`).
- **Job**: A set of steps in a workflow that is executed on the same runner. Jobs run in parallel by default but can be made sequential.
- **Step**: An individual task that can run commands (shell) or an action.
- **Action**: A standalone command that is combined into steps to create a job.
- **Runner**: A server that runs your workflows when they're triggered.

---

## 2. CI/CD Principles
- **Continuous Integration (CI)**: Merging all developer working copies to a shared mainline several times a day. Automating builds and tests.
- **Continuous Deployment (CD)**: Automatically deploying code to production after passing the CI pipeline.

---

## 3. Workflow Syntax (YAML)
Workflows are defined in `.github/workflows/`.
```yaml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: npm test
```

---

## 4. Advanced Features
- **Secrets**: Storing sensitive information (API keys, passwords) securely in GitHub settings and accessing them in workflows via `${{ secrets.NAME }}`.
- **Matrix Builds**: Running a job across multiple versions of a language or operating system simultaneously.
- **Environments & Approvals**: Setting up deployment environments that require manual approval before a workflow can proceed.

---

## 5. Self-Hosted vs. GitHub-Hosted Runners
- **GitHub-Hosted**: Easy to use, maintained by GitHub, but have limited resources and customization.
- **Self-Hosted**: You maintain the runner, providing full control over hardware and software, but with added maintenance overhead.

## Common Interview Questions
- **"What is a CI/CD pipeline?"**: An automated sequence of steps to build, test, and deploy software.
- **"How do you handle secrets in GitHub Actions?"**: Use GitHub Secrets and reference them in the YAML file using the `secrets` context.
- **"Explain the difference between a Job and a Step."**: A Job is a group of Steps running on one runner. Steps are individual tasks within a Job.

## Related Topics
- [[01_foundations/02_sdlc|SDLC (Agile & DevOps)]]
- [[08_stack_deep_dives/04_devops_cloud_stack/03_terraform_iac|Terraform]]
