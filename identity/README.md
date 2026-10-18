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

```
uv run uvicorn main:app --reload
```

Then check `http://localhost:8000/health`.
