# 0004. Synchronous call now, events later

- **Status:** Accepted
- **Date:** 2026-10-15

## Context

The ledger enforces the visibility rule, which depends on knowing which household a user belongs to. That information is owned by the household service. A decision is needed on how the ledger gets it.

## Alternatives considered

- Embed the household id in the JWT issued by identity. Rejected: a token is carried around until it expires, but household membership can change at any time (joining or leaving), so the token would go stale and the ledger would enforce visibility against outdated membership.
- Build on Kafka from the start, with household publishing membership events and the ledger keeping a local read-only copy. Rejected for now: Kafka doesn't exist yet in this project, it's deliberately deferred to a later milestone, and starting with events here would skip past actually feeling the pain of synchronous coupling between services, which is the point of introducing messaging in stages instead of upfront.

## Decision

For v0, the ledger calls the household service synchronously over HTTP whenever it needs a user's household. When Kafka is introduced later, this becomes membership events published by household, and the ledger keeps a local copy of "user X belongs to household Y", built from those events.

## Consequences

v0 stays simple to implement and reason about, with the coupling living in one obvious place. It also means the ledger becomes unavailable, or has to degrade its visibility checks, if household is down. That limitation is intentional: the plan is to feel this failure mode before fixing it with events, not to avoid it. The later move to events is a planned migration, not a correction of a mistake, so it's budgeted for from the start rather than treated as a surprise.
