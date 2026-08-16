# Finance Tracker
 
Personal and household finance tracker built with FastAPI. Study project for senior backend roles.
 
## Stack
 
Python 3.14, FastAPI, SQLAlchemy 2.0 (async), PostgreSQL 18, Alembic, Docker Compose
 
## Setup
 
```bash
cp .env.example .env       # fill in your own values
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
alembic upgrade head
uvicorn app.main:app --reload
```
 