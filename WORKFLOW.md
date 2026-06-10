# PrepVault Code Workflow

## Repository
- **Remote**: `mrxsierra/CS`
- **Local**: `/home/team/shared/` (git root)
- **Vault content**: `/home/team/shared/prepvault/`

## Commit Strategy: Milestone-Based
We commit after every major milestone or completed task. Each commit should represent a coherent unit of work.

### Commit Message Format
```
type(scope): brief description

[optional body with details]
```

**Types**: `feat` (new content/topic), `update` (existing content improved), `fix` (correction), `docs` (documentation), `chore` (config/setup)

**Examples**:
- `feat(dsa): add 12-pattern matrix to DSA landing page`
- `feat(foundations): add Language Internals module (JS, Java, Python, Go)`
- `update(roles): enhance all role tracks with 2026-27 market realities`
- `chore(vault): add .obsidian config and CSS snippets`

## Branch Strategy
- Push directly to `main` for content-only changes (this is a knowledge vault, not application code)
- Use feature branches only when multiple members need to coordinate on conflicting changes

## Pull Requests
Not required for content additions — push directly. Use PRs only for structural changes that need review.

## After Each Completed Task
1. Stage all relevant changes
2. Commit with a clear milestone message
3. Push to origin/main