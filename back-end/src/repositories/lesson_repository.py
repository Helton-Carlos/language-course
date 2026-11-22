from collections.abc import Sequence
from typing import Any
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.lesson import Lesson


class LessonRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list_by_user(self, user_id: UUID) -> Sequence[Lesson]:
        result = await self._session.scalars(
            select(Lesson).where(Lesson.user_id == user_id).order_by(Lesson.created_at.desc())
        )
        return result.all()

    async def get(self, user_id: UUID, lesson_id: UUID) -> Lesson | None:
        return await self._session.scalar(
            select(Lesson).where(Lesson.user_id == user_id, Lesson.id == lesson_id)
        )

    async def add(self, values: dict[str, Any]) -> Lesson:
        lesson = Lesson(**values)
        self._session.add(lesson)
        await self._session.commit()
        await self._session.refresh(lesson)
        return lesson

    async def delete(self, lesson: Lesson) -> None:
        await self._session.delete(lesson)
        await self._session.commit()
