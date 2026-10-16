# 0001. Monorepo

- **Status:** Accepted
- **Date:** 2026-10-15

## Context

The system is split into three services (identity, household, ledger) from the start, built by a single developer as a study project. A repository layout has to be picked before any code exists: one repository per service, or a single repository holding all of them.

## Alternatives considered

- One repository per service (polyrepo). This mirrors how many companies structure microservices and gives each service a clean, isolated deployment pipeline. For a solo developer still shaping service boundaries, though, it means context switching between repos, duplicated tooling config (lint, type checker, CI) in three places, and no way to make an atomic change that touches two services at once if a boundary turns out to be wrong.

## Decision

Use a single repository with one folder per service, plus folders for shared code and infrastructure.

## Consequences

Easier to evolve the system while service boundaries are still settling, since a single pull request can touch more than one service when needed. Shared tooling config lives in one place instead of three. The trade-off: the repo doesn't simulate the deployment independence that separate repos would give each service, which is one of the things this project explicitly wants to feel the lack of before reaching for it. Each service still only reads its own database and talks to others only through HTTP or, later, events, so the monorepo doesn't weaken the logical separation between services, only the repository-level one. Worth revisiting if the project ever needs independent release cadences per service.
