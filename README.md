# Finance Tracker
 
Personal and household finance tracker built with Django. Study project for senior backend roles.
 
## Stack
 
Python 3.14, Django 5.2, PostgreSQL 18, Docker Compose
 
## Setup
 
```bash
cp .env.example .env       # fill in your own values
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
python manage.py migrate
python manage.py runserver
```
 