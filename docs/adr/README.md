# Architecture Decision Records

Each ADR records an architecture decision: the context, what was decided, and the consequences. Use the [template](0000-template.md) and number sequentially.

## Possible statuses

- **Proposed**: under discussion
- **Accepted**: in effect
- **Superseded**: replaced by a newer ADR, which must be referenced

## Index

| No. | Title | Status |
| --- | --- | --- |
| [0001](0001-monorepo.md) | Monorepo | Accepted |
| [0002](0002-database-per-service.md) | One database per service | Accepted |
| [0003](0003-ledger-owns-accounts-and-transactions.md) | Accounts and transactions together in the ledger | Accepted |
| [0004](0004-synchronous-call-then-events.md) | Synchronous call now, events later | Accepted |
| [0005](0005-kafka-over-rabbitmq.md) | Kafka instead of RabbitMQ | Accepted |
| [0006](0006-aws-over-gcp.md) | AWS instead of GCP | Accepted |
