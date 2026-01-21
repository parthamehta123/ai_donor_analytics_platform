.PHONY: help install dev test lint format run up down rebuild logs clean

help:
	@echo "Available commands:"
	@echo "  make install   Install dependencies"
	@echo "  make dev       Install deps + editable mode"
	@echo "  make run       Run FastAPI locally"
	@echo "  make test      Run pytest suite"
	@echo "  make lint      Run ruff linter"
	@echo "  make format    Autoformat with ruff"
	@echo "  make up        Start docker-compose stack"
	@echo "  make down      Stop docker-compose stack"
	@echo "  make rebuild   Rebuild docker images"
	@echo "  make logs      Tail docker logs"
	@echo "  make clean     Remove __pycache__ and temp files"

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements.txt
	pip install -e .

run:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	ruff .

format:
	ruff . --fix

up:
	docker compose up --build

down:
	docker compose down

rebuild:
	docker compose build --no-cache

logs:
	docker compose logs -f

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
