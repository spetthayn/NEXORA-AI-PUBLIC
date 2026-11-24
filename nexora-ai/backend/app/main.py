"""NEXORA AI FastAPI application — Phase 8 (PAPER default, controlled LIVE gate).

Run:
  PYTHONPATH=. uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000

This app is separate from backend.api.minimal_app (OpenAPI contract surface for Phase 0).
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routers import system, market_data, quant, ai, studio, research, adaptive, paper, replay, execution, monitoring
from backend.app.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=(
        "NEXORA AI Phase 8. Controlled PAPER→LIVE gate. Secrets from env only. "
        "Simulation default. No real sandbox exchange orders."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system.router)
app.include_router(market_data.router)
app.include_router(quant.router)
app.include_router(ai.router)
app.include_router(studio.router)
app.include_router(research.router)
app.include_router(adaptive.router)
app.include_router(paper.router)
app.include_router(replay.router)
app.include_router(execution.router)
app.include_router(monitoring.router)


@app.get("/")
def root() -> dict:
    return {
        "name": settings.app_name,
        "phase": settings.phase,
        "version": settings.version,
        "docs": "/docs",
        "simulation_only": settings.simulation_only,
    }
