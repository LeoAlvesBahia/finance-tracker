# v0 overview

## Behavior

- A user exists on their own and controls their own finances. No household is required.
- A household is optional: it's a group with members. Creating a household creates no accounts, and a household can have zero shared accounts.
- A membership links a user and a household, in its own table. In v0, each user can belong to at most one household. This is enforced as a validation, not a structural limit, so the model can support multiple households later without a migration.
- A household is created by a member, who adds the other member directly by their email. There's no invite/accept flow. There are no roles (admin/member) in v0, every member is equal.
- An account has exactly one owner: a user (personal account, visible only to them) or a household (shared account, visible and postable by every member). No credit cards in v0.
- A transaction inherits its account's visibility. It never has a rule of its own.
- Visibility rule: a user can see an account if they own it, or if the owner is the household they belong to. The other member has no way of knowing a personal account exists.
- Categories: a fixed list, the same for every user. Customization comes later.
- Monthly summaries: the household summary shows only shared accounts. "My summary" shows my personal accounts plus my household's shared accounts. Private accounts never enter the household total, so they can't leak by deduction.
- Data entry: manual only, to start.
- No transfers between accounts in v0, so balances are approximate whenever money actually moves between accounts in real life. This is the first increment planned after the basics.
- Single currency (BRL), values always in integer cents.
- Expected users: two, within a single household, to start. Nothing in the model limits it to that number.

## Out of scope for v0

- API gateway
- Schema registry (Avro/Protobuf), starting instead with a versioned JSON envelope
- Redis
- Custom categories
- Credit cards
- Transfers between accounts
- Household invite/accept flow and roles (admin/member)
