# 0006. AWS instead of GCP

- **Status:** Accepted
- **Date:** 2026-10-15

## Context

The project needs a cloud provider for the milestone where it leaves local-only infrastructure. GCP was the original choice, before switching to AWS.

## Alternatives considered

- GCP. A reasonable fit, with direct equivalents for everything planned (Cloud Run, Cloud SQL, GKE, Artifact Registry) and a free tier. Less represented in the job market than AWS, though.

## Decision

AWS, chosen primarily because it has a larger market share and shows up more often in job postings. This follows the same principle already used for Kafka over RabbitMQ: pick the technology most commonly demanded, not the one that's simplest to run.

## Consequences

AWS free tier rules are different from GCP's and need to be revalidated on the official page once the cloud milestone starts, nothing gets created in AWS before then. The planned AWS equivalents for what the GCP services would have covered: Cloud Run becomes ECS Fargate or App Runner, Cloud SQL becomes RDS, GKE becomes EKS, Artifact Registry becomes ECR. No infrastructure exists yet for either provider, so this is a decision made ahead of time, not a migration.
