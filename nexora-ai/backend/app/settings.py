"""Application settings — Phase 8 settings."""

from __future__ import annotations

import os


class Settings:
    """Simple settings object. Secrets only via environment when LIVE is enabled."""

    app_name: str = "NEXORA AI"
    phase: str = "8"
    version: str = "0.8.0-phase8"
    simulation_only: bool = True

    def __init__(self) -> None:
        raw = os.environ.get(
            "NEXORA_CORS_ORIGINS",
            "http://localhost:5173,http://127.0.0.1:5173",
        )
        self.cors_origins: list[str] = [o.strip() for o in raw.split(",") if o.strip()]


settings = Settings()
