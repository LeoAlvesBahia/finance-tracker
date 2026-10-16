# 0005. Kafka instead of RabbitMQ

- **Status:** Accepted
- **Date:** 2026-10-15

## Context

The project wants to learn a messaging technology that's widely used in the market, as a step toward event-driven communication between services (see [0004](0004-synchronous-call-then-events.md)). A choice has to be made between the common options.

## Alternatives considered

- RabbitMQ. Simpler to run locally and lighter on resources, and well suited to task-queue style messaging. It shows up less often, though, in job postings specifically framed around event streaming and event-driven architecture, which is what this project wants to practice.
- A cloud-managed pub/sub service. Removes the operational learning entirely, which defeats the purpose of running messaging locally as part of this study project.

## Decision

Kafka, running in KRaft mode (no ZooKeeper), chosen specifically because it's the more in-demand skill for the kind of event-driven work this project is practicing, even though it's heavier to operate than RabbitMQ for a solo developer.

## Consequences

Higher local operational cost than RabbitMQ, more moving parts to run and monitor, accepted as the price of practicing the more market-relevant tool. KRaft mode removes the ZooKeeper dependency, keeping the setup one component lighter than older Kafka deployments. Kafka's introduction is deferred to a later milestone, so this cost gets paid once the domain and basic cloud setup are already stable, not on day one.
