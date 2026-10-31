import asyncio

from pwdlib import PasswordHash

_password_hash = PasswordHash.recommended()


async def hash_password(password: str) -> str:
    return await asyncio.to_thread(_password_hash.hash, password)


async def verify_password(password: str, hashed: str) -> bool:
    return await asyncio.to_thread(_password_hash.verify, password, hashed)
