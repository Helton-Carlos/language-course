import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL

BACK_END_DIR = Path(__file__).resolve().parents[2]

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


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DB_",
        env_file=BACK_END_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: SecretStr
    name: str = "language_data"

    @property
    def url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.name,
        )


@lru_cache
def get_database_settings() -> DatabaseSettings:
    return DatabaseSettings()  # type: ignore[call-arg]


class AuthSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="AUTH_",
        env_file=BACK_END_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    secret_key: SecretStr
    algorithm: str = "HS256"
    access_token_minutes: int = 60
    cookie_name: str = "access_token"
    cookie_secure: bool = False


@lru_cache
def get_auth_settings() -> AuthSettings:
    return AuthSettings()  # type: ignore[call-arg]
