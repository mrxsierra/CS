---
type: concept
tags: [foundations, git, version-control, architecture]
created: 2026-06-10
---

# Git Architecture & Internals

Understanding Git's internals is a common "Senior Engineer" interview topic. It demonstrates that you understand the tools you use every day.

---

## 1. The Three States
Git has three main states that your files can reside in:
- **Working Directory**: The local sandbox where you make changes.
- **Staging Area (Index)**: A file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **Git Directory (Repository)**: Where Git stores the metadata and object database for your project.

## 2. Git Objects (The Directed Acyclic Graph)
Git is essentially a content-addressed filesystem. It uses four types of objects stored in `.git/objects`:

### Blobs (Binary Large Objects)
- Stores the **content** of a file.
- Does not store the filename or metadata.
- If two files have the same content, they share the same blob.

### Trees
- Stores the **directory structure**.
- Maps filenames to blobs or other trees.
- Represents a "snapshot" of a directory.

### Commits
- Points to a root **Tree** object (the snapshot of the project).
- Contains metadata: author, committer, timestamp, and message.
- Points to zero or more **parent commits**.

### Tags
- A permanent label for a specific commit (e.g., `v1.0.0`).

## 3. The Power of Content Addressing (SHA-1)
Git identifies every object by its SHA-1 hash (a 40-character hexadecimal string).
- **Immutability**: If the content changes, the hash changes. Git never overwrites data; it only adds new objects.
- **Deduplication**: Identical content across different files or commits is only stored once.

## 4. Branching and Merging
- **Branches**: Simply a lightweight movable pointer to a commit.
- **HEAD**: A pointer to the current branch you are on.
- **Fast-Forward Merge**: When the target branch is a direct ancestor of the source branch.
- **Three-Way Merge**: When history has diverged; Git creates a new "merge commit" with two parents.

## 5. Rebase vs. Merge
- **Merge**: Preserves history exactly as it happened. Creates a non-linear history if branches diverged.
- **Rebase**: Rewrites history by applying changes from one branch onto another. Results in a clean, linear history. 
- **Rule of Thumb**: Never rebase public branches that others are working on.

## Common Interview Questions
- **"What happens when you run `git commit`?"**: Explain the transition from working directory -> staging -> object database (blob creation, tree creation, commit creation).
- **"How does Git handle file renames?"**: It doesn't explicitly track renames; it detects them by comparing blobs (content similarity).
- **"What is a 'detached HEAD'?"**: When HEAD points directly to a commit instead of a branch pointer.

## Role-Specific Applications
- **Frontend/Backend**: Trunk-based development, handling merge conflicts in generated code (e.g., `package-lock.json`), using interactive rebase to clean up feature branches before PR.
- **DevOps**: Managing infrastructure as code (IaC), GitOps patterns (ArgoCD/Flux), implementing branch protection rules and automated CI triggers.
- **ML Engineer**: Versioning datasets and models using DVC (Data Version Control) which mimics Git architecture for large files.
- **Security**: Auditing commit history for secrets, signing commits with GPG, understanding `git filter-repo` to purge sensitive data from history.

## Related Topics
- [[01_Foundations/02_SDLC|SDLC (CI/CD)]]
- [[01_Foundations/03_System_Design|System Design (Storage)]]
