# identity

Sign-up, login, and JWT issuance for Finance Tracker.

## Development

Requires [uv](https://docs.astral.sh/uv/).

```
uv run ruff check .   # lint
uv run pyright        # type check
uv run pytest         # run tests
```

## Run

Requires Docker, for the database.

```
docker compose up --build
```

(Run from the repo root, not this folder, `docker-compose.yml` orchestrates `identity` together with its Postgres.)

Then check `http://localhost:8000/health`, or see `requests.http` (open with the REST Client extension) for example requests against `/signup`.

## Testing

`uv run pytest` also requires Docker to be running, the integration test spins up a real, disposable Postgres via `testcontainers` for the duration of the test run.
