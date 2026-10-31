from collections.abc import Sequence
from typing import Any
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.exceptions import LanguageCodeAlreadyExistsError
from models.language import Language


class LanguageRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list_all(self) -> Sequence[Language]:
        result = await self._session.scalars(select(Language).order_by(Language.name_pt))
        return result.all()

    async def get(self, language_id: UUID) -> Language | None:
        return await self._session.get(Language, language_id)

    async def get_by_code(self, code: str) -> Language | None:
        return await self._session.scalar(select(Language).where(Language.code == code))

    async def add(self, values: dict[str, Any]) -> Language:
        language = Language(**values)
        self._session.add(language)
        await self._commit()
        await self._session.refresh(language)
        return language

    async def update(self, language: Language, values: dict[str, Any]) -> Language:
        for field, value in values.items():
            setattr(language, field, value)
        await self._commit()
        await self._session.refresh(language)
        return language

    async def delete(self, language: Language) -> None:
        await self._session.delete(language)
        await self._commit()

    async def _commit(self) -> None:
        try:
            await self._session.commit()
        except IntegrityError as exc:
            await self._session.rollback()
            raise LanguageCodeAlreadyExistsError() from exc
