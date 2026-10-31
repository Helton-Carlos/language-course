import asyncio
from datetime import UTC, datetime, timedelta
from uuid import UUID

import jwt
from pwdlib import PasswordHash

from core.config import get_auth_settings

_password_hash = PasswordHash.recommended()

DUMMY_HASH = _password_hash.hash("senha-ficticia-para-igualar-o-tempo")


async def hash_password(password: str) -> str:
    return await asyncio.to_thread(_password_hash.hash, password)


async def verify_password(password: str, hashed: str) -> bool:
    return await asyncio.to_thread(_password_hash.verify, password, hashed)


def create_access_token(user_id: UUID) -> str:
    settings = get_auth_settings()
    expires_at = datetime.now(UTC) + timedelta(minutes=settings.access_token_minutes)
    return jwt.encode(
        {"sub": str(user_id), "exp": expires_at},
        settings.secret_key.get_secret_value(),
        algorithm=settings.algorithm,
    )


def decode_access_token(token: str) -> UUID | None:
    settings = get_auth_settings()
    try:
        payload = jwt.decode(
            token,
            settings.secret_key.get_secret_value(),
            algorithms=[settings.algorithm],
            options={"require": ["exp", "sub"]},
        )
        return UUID(payload["sub"])
    except (jwt.PyJWTError, ValueError, TypeError):
        return None
