from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Donor Analytics Platform",
    version="0.1.0",
    description="FastAPI + RAG + MCP + RBAC demo service",
)

app.include_router(router)
