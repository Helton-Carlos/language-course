import argparse
import asyncio
import getpass
import os
import secrets
import sys

from core.database import SessionLocal, dispose_engine
from core.exceptions import AppError
from repositories.user_repository import UserRepository
from schemas.user import UserCreate
from services.user_service import UserService


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="admin")
    parser.add_argument("--email", default="adm@gmail.com")
    parser.add_argument("--generate", action="store_true")
    return parser.parse_args()


def resolve_password(generate: bool) -> tuple[str, bool]:
    if generate:
        return secrets.token_urlsafe(16), True
    password = os.getenv("ADMIN_PASSWORD") or getpass.getpass("Senha do admin: ")
    return password, False


async def main() -> int:
    args = parse_args()
    password, generated = resolve_password(args.generate)

    try:
        async with SessionLocal() as session:
            service = UserService(UserRepository(session))
            data = UserCreate(name=args.name, email=args.email, password=password)
            user = await service.create_user(data, role="admin")
    except AppError as exc:
        print(exc.detail)
        return 1
    finally:
        await dispose_engine()

    print(f"Admin criado: {user.email} ({user.id})")
    if generated:
        print(f"Senha gerada (guarde agora, ela não será exibida de novo): {password}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
