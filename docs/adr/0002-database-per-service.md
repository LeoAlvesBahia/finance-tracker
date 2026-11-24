# 0002. One database per service

- **Status:** Accepted
- **Date:** 2026-10-15

## Context

Each of the three services (identity, household, ledger) owns its own data: users and credentials, households and memberships, accounts and transactions. A decision is needed on whether they share one database or each gets its own.

## Alternatives considered

- A single shared database for all three services. Lower operational overhead and easy cross-service joins (for example, joining a household's membership straight into a ledger query). It also creates implicit coupling: any service could read or write another service's tables, a schema change in one service can silently break another, and the database becomes a shared backend that defeats the point of learning real service boundaries.

## Decision

Each service gets its own PostgreSQL database. No service reads another service's database directly. Services only talk to each other over HTTP (and later, events). References to another service's data are plain UUIDs, with no foreign key enforced at the database level.

## Consequences

Each service's schema evolves independently, without coordinating migrations with the others. Dropping cross-service foreign keys forces the application layer to validate references explicitly, for example the ledger has to confirm a household UUID is real through an HTTP call instead of relying on a database constraint, which is closer to how real distributed systems behave. The trade-off is the loss of cross-service joins and database-enforced referential integrity: if a household is deleted while a ledger account still references it, nothing in the database stops that, and the application has to decide what that means.
