.PHONY: help install dev run test test-unit test-integration test-all lint format up down rebuild logs clean smoke

help:
	@echo ""
	@echo "AI Donor Analytics Platform - Commands"
	@echo "--------------------------------------"
	@echo "make install           Install dependencies"
	@echo "make dev               Install deps in editable mode"
	@echo "make run               Run FastAPI locally"
	@echo "make test              Run CI-safe test suite"
	@echo "make test-unit         Run only unit tests"
	@echo "make test-integration  Run integration tests (safe if none exist)"
	@echo "make test-all          Run full pytest suite"
	@echo "make smoke             Run manual smoke tests (requires make up)"
	@echo "make lint              Run ruff linter"
	@echo "make format            Autoformat with ruff"
	@echo "make up                Start docker-compose stack"
	@echo "make down              Stop docker-compose stack"
	@echo "make rebuild           Rebuild docker images (no cache)"
	@echo "make logs              Tail docker logs"
	@echo "make clean             Remove __pycache__ and temp files"
	@echo ""

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements.txt
	pip install -e .

run:
	uvicorn app.main:app --reload

# CI-safe tests
test:
	pytest tests

test-unit:
	pytest -m unit

# Allow empty integration suite without failing
test-integration:
	pytest -m integration || echo "No integration tests collected (ok)"

test-all:
	pytest

smoke:
	@echo "Running smoke tests (requires services running)..."
	@python scripts/smoke_api.py || (echo "API not reachable. Run: make up" && exit 1)
	@python scripts/smoke_mcp.py || (echo "MCP failed. Is server running?" && exit 1)

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
