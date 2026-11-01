from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.placement_question import PlacementQuestion


class PlacementRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list_by_level(self, language_id: UUID, level: str) -> Sequence[PlacementQuestion]:
        result = await self._session.scalars(
            select(PlacementQuestion).where(
                PlacementQuestion.language_id == language_id,
                PlacementQuestion.level == level,
            )
        )
        return result.all()

    async def has_questions(self, language_id: UUID, level: str) -> bool:
        total = await self._session.scalar(
            select(func.count())
            .select_from(PlacementQuestion)
            .where(
                PlacementQuestion.language_id == language_id,
                PlacementQuestion.level == level,
            )
        )
        return bool(total)
