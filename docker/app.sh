#!/bin/zsh
alembic upgrade head

gunicorn quiz_service.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
