FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim AS builder
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev
COPY main.py ./

FROM python:3.14-slim-trixie
WORKDIR /app
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"
RUN groupadd --system app && useradd --system --gid app app
RUN chown -R app:app /app
USER app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]