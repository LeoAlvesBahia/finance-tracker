# 0007. Services trust a JWT signed by identity with an asymmetric key

- **Status:** Accepted
- **Date:** 2026-11-25

## Context

Identity checks a user's password at login. After that, every request to household and ledger has to answer two questions: is this request really from a logged-in user, and which user is it? Each service has its own database (see [0002](0002-database-per-service.md)), so household and ledger can't look up sessions in identity's tables. Calling identity on every request would make identity a hard dependency of every operation in the system, on top of the household call the ledger already makes (see [0004](0004-synchronous-call-then-events.md)).

## Alternatives considered

- Opaque tokens checked by calling identity on every request (token introspection). Revoking a token takes effect immediately, but every request to household or ledger becomes an extra network call, and if identity is down, nothing works.
- A JWT signed with a shared secret (HS256). Verification is local and fast, but the same secret both signs and verifies. Household and ledger would need a copy of it, which means any of them could also create valid tokens for any user. One compromised service compromises all of them.
- Distributing the public key through configuration (an environment variable in each service). Simple, but changing the key means redeploying every service at the same moment, so in practice the key would never be rotated.

## Decision

Identity issues JWTs signed with RS256, an asymmetric algorithm. Only identity holds the private key. It publishes the matching public key at `/.well-known/jwks.json`, in the standard JWKS format, and each token carries a `kid` header saying which key signed it. Household and ledger fetch the JWKS at startup, cache it, fetch it again when they see an unknown `kid`, and verify every token locally.

Tokens contain only:

- `sub`: the user id
- `iss`: who issued the token (identity)
- `aud`: who the token is meant for (the finance-tracker API)
- `iat`: when it was issued
- `exp`: when it expires, 60 minutes after `iat`

The household id is deliberately not in the token, for the reason given in [0004](0004-synchronous-call-then-events.md): membership can change while a token is still valid. Every service rejects a token whose signature, `iss`, `aud` or `exp` doesn't check out.

## Consequences

Household and ledger verify tokens without any network call, so they keep authenticating requests even while identity is down, as long as they have the keys cached. Only identity can create tokens, so a compromised household or ledger can't impersonate users. Keys can be rotated without redeploying anything: publish the new key next to the old one, start signing with the new one, and remove the old one after the longest token lifetime (60 minutes) has passed.

The trade-off is that a token can't be revoked before it expires. Logging out only means the client throws the token away, and a deactivated user, or a stolen token, keeps working for up to 60 minutes. For v0, with two known users, that risk is accepted. Revocation will come in two planned steps. First, short-lived access tokens (5 to 15 minutes) plus refresh tokens stored by identity: revoking means deleting the refresh token, so access ends when the current access token expires, still without a call to identity on every request. Then, once Kafka exists, identity publishes events like "user deactivated" and each service keeps a local list of blocked users, the same pattern [0004](0004-synchronous-call-then-events.md) plans for membership, which makes revocation close to immediate. A shared denylist checked on every request was set aside, because it brings back a lookup per request and a new dependency (Redis) that v0 doesn't have. The private key has to be stored as a secret: a local file kept out of git for now, and a managed secret store once the project moves to AWS.
