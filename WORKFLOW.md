# PrepVault Code Workflow

## Repository
- **Remote**: `https://github.com/mrxsierra/CS.git` (HTTPS with stored credentials)
- **Local**: `/home/team/shared/` (git root)
- **Vault content**: `/home/team/shared/prepvault/`
- **Credentials**: Stored in `~/.git-credentials` (600 permissions)
- **Lead push command**: `git push` (no auth needed — credentials stored)

## Commit Strategy: Milestone-Based
Commit after every major milestone or completed task. Each commit represents a coherent unit of work.

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
1. Stage all relevant changes: `cd /home/team/shared && git add -A`
2. Commit with a clear milestone message: `git commit -m "type(scope): description"`
3. Push to origin/main: `git push`