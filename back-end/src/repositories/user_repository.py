from collections.abc import Sequence
from typing import Any
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.exceptions import UserEmailAlreadyExistsError
from models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list_all(self) -> Sequence[User]:
        result = await self._session.scalars(select(User).order_by(User.name))
        return result.all()

    async def get(self, user_id: UUID) -> User | None:
        return await self._session.get(User, user_id)

    async def get_by_email(self, email: str) -> User | None:
        return await self._session.scalar(select(User).where(User.email == email))

    async def add(self, values: dict[str, Any]) -> User:
        user = User(**values)
        self._session.add(user)
        await self._commit()
        await self._session.refresh(user)
        return user

    async def update(self, user: User, values: dict[str, Any]) -> User:
        for field, value in values.items():
            setattr(user, field, value)
        await self._commit()
        await self._session.refresh(user)
        return user

    async def delete(self, user: User) -> None:
        await self._session.delete(user)
        await self._commit()

    async def _commit(self) -> None:
        try:
            await self._session.commit()
        except IntegrityError as exc:
            await self._session.rollback()
            raise UserEmailAlreadyExistsError() from exc
