# Contributing

## Prerequisites

- [uv](https://docs.astral.sh/uv/) for Python tooling
- Docker, for building and running services
- git
- [GitHub CLI](https://cli.github.com/) (`gh`), used for issues, PRs, and the project board

## Getting started

Clone the repo, then open `finance-tracker.code-workspace` in VS Code (File → Open Workspace from File), not just the folder.

This matters: the workspace file is what tells editor tooling (Ruff, in particular) to treat each service as its own project. Opening the plain folder instead will make linting and formatting misbehave across service boundaries.

## Per-service setup

Each service manages its own dependencies independently, there's no single repo-wide install step. For `identity`:

```
cd identity
uv sync
```

Each service's own `README.md` has its specific run, lint, type-check, and test commands.

## Workflow

Issue on the GitHub Project board, branch created from the issue page ("Create a branch"), code, PR, merge. `main` is protected, no direct pushes, not even for admins.
