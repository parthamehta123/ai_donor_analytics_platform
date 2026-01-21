# AI Donor Analytics Platform

![Python](https://img.shields.io/badge/python-3.12+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-green)
![Tests](https://img.shields.io/badge/tests-pytest-success)
![Docker](https://img.shields.io/badge/docker-compose-blue)
![MCP](https://img.shields.io/badge/MCP-integrated-purple)

A **portfolio-grade AI backend platform** demonstrating how to build
real-world AI systems with:

-   FastAPI production API design
-   Role-based access control (RBAC)
-   Retrieval Augmented Generation (RAG)
-   Model Context Protocol (MCP) server
-   PostgreSQL integration
-   Typed business layer (Pydantic models)
-   Unit + integration tests
-   Dockerized infra

This is not a notebook demo. It is a **production-style service**.

------------------------------------------------------------------------

## Architecture Overview

    Client / Browser / Swagger UI
            |
            v
         FastAPI API Layer (RBAC, Validation, Schemas)
            |
            +--> Business Tools Layer (app/tools.py)
            |        - Typed models
            |        - Caching
            |        - Validation
            |
            +--> DB Access Layer (Postgres via psycopg)
            |
            +--> RAG Pipeline
            |        - SentenceTransformers embeddings
            |        - FAISS vector search
            |
            +--> MCP Server (stdio protocol)
                     - campaign_performance tool
                     - donor_retention tool
                     - ask_docs RAG tool

    Docker Compose
      ├── FastAPI container
      ├── MCP server container
      └── Postgres container (seeded)

------------------------------------------------------------------------

## Features Demonstrated

-   Typed API schemas with OpenAPI
-   Role-based authorization via headers
-   Clean separation: API → Tools → DB
-   RAG with vector search
-   MCP server usable by Claude Desktop / VSCode agents
-   Pytest unit tests for:
    -   Tools layer
    -   RAG
    -   DB contract
    -   FastAPI endpoints
    -   MCP tools
-   Docker Compose local environment

------------------------------------------------------------------------

## Quickstart

``` bash
# Build and run
make up

# Run tests
make test

# Stop services
make down
```

Open Swagger UI:

    http://localhost:8000/docs

Example API call:

``` bash
curl -H "x-role: analyst" "http://localhost:8000/tools/campaign-performance?client_id=abc"
```

------------------------------------------------------------------------

## Role Based Access Examples

  Endpoint                      Required Role
  ----------------------------- ---------------
  /tools/campaign-performance   analyst
  /tools/donor-retention        strategist
  /rag/ask                      public

------------------------------------------------------------------------

## Manual Smoke Tests (Local Only)

This project includes optional manual smoke scripts for validating the full system locally.

These are intentionally not part of pytest because they require:
- Running Docker services
- Real PostgreSQL container
- Real FastAPI process
- MCP runtime

Location:
- scripts/smoke_api.py
- scripts/smoke_mcp.py

Run locally:

```bash
make up

python scripts/smoke_api.py
python scripts/smoke_mcp.py
```

These validate:
- End-to-end API → DB behavior
- RBAC enforcement
- MCP tool execution
- RAG responses

------------------------------------------------------------------------

## MCP Integration

The project includes a fully working MCP server:

``` bash
python -m app.mcp.server
```

Registered tools: - campaign_performance(client_id) -
donor_retention(client_id) - ask_docs(question)

This allows AI agents (Claude Desktop, VSCode agents) to directly call
your backend.

------------------------------------------------------------------------

## Claude Desktop MCP Config

Create:

    docs/claude_mcp_config.json

``` json
{
  "mcpServers": {
    "donor-analytics": {
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["-u", "-m", "app.mcp.server"],
      "cwd": "/absolute/path/to/ai_donor_analytics_platform"
    }
  }
}
```

Claude Desktop → Settings → Developer → MCP Servers → Load config.

------------------------------------------------------------------------

## VSCode MCP Config

Create:

    docs/vscode_mcp.json

``` json
{
  "servers": {
    "donor-analytics": {
      "type": "stdio",
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["-u", "-m", "app.mcp.server"],
      "cwd": "/absolute/path/to/ai_donor_analytics_platform"
    }
  }
}
```

------------------------------------------------------------------------

## Makefile

``` makefile
up:
    docker compose up --build

down:
    docker compose down

test:
    pytest

lint:
    ruff .
```

------------------------------------------------------------------------

## Folder Structure

    ai_donor_analytics_platform/
    ├── app/
    │   ├── api/routes.py      # API layer
    │   ├── db/queries.py       # DB access
    │   ├── rag/                # RAG pipeline
    │   ├── models.py           # Typed schemas
    │   ├── tools.py            # Business layer
    │   ├── security.py         # RBAC logic
    │   └── main.py             # App entrypoint
    │
    ├── app/mcp/server.py       # MCP server
    ├── db/init.sql             # Seed data
    ├── tests/                  # pytest suite
    ├── docker-compose.yml
    ├── Dockerfile
    ├── Makefile
    ├── docs/
    │   ├── claude_mcp_config.json
    │   └── vscode_mcp.json
    └── README.md

------------------------------------------------------------------------

## One-Paragraph Project Pitch

> I built a production-style AI analytics backend using FastAPI,
> PostgreSQL, and Retrieval Augmented Generation. The system exposes
> typed APIs with role-based access control, integrates a vector-based
> RAG pipeline for document Q&A, and provides an MCP server so AI agents
> like Claude Desktop or VSCode copilots can directly invoke real tools.
> The entire system is dockerized with seeded infrastructure and
> includes a comprehensive pytest suite covering APIs, tools, database
> contracts, and MCP behavior. The project is designed to showcase
> real-world AI platform engineering rather than notebook-level
> experimentation.
