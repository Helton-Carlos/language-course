import os
from dataclasses import dataclass, field
from functools import lru_cache

DEFAULT_CORS_ORIGINS = "http://localhost:3001,http://127.0.0.1:3001"

def _split(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


@dataclass(frozen=True)
class Settings:
    app_title: str = "Language Course API"
    api_prefix: str = "/api"
    cors_origins: list[str] = field(
        default_factory=lambda: _split(os.getenv("CORS_ORIGINS", DEFAULT_CORS_ORIGINS))
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
