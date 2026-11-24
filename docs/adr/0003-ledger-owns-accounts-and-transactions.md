# 0003. Accounts and transactions together in the ledger

- **Status:** Accepted
- **Date:** 2026-10-15

## Context

An account has an owner (a user or a household) and a visibility rule derived from that owner. A transaction always inherits its account's visibility and never has a rule of its own. Balances are computed from transactions against their account. A decision is needed on whether accounts and transactions belong to the same service or to two separate ones.

## Alternatives considered

- Separate "accounts" service and "transactions" service. This is the classic mistake of drawing a service boundary around tables instead of around a business capability. Visibility, balance calculation, and nearly every operation depend on both an account and its transactions together. Splitting them would mean a synchronous call between the two services for almost every read and write, recreating a single bounded context as two services connected by constant chatty calls.

## Decision

The ledger service owns accounts, transactions, and the fixed category list together.

## Consequences

Balance calculation and visibility enforcement stay local to one service, with no network call needed for core ledger operations. The service boundary mirrors the real business concept, a ledger, instead of a database table split. The trade-off is that the ledger service carries more responsibility and complexity than identity or household, which is expected: it's where the real complexity of the domain lives, and it shouldn't be hidden by forcing an artificial split.
