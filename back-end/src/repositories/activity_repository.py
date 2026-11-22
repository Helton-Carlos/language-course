from collections.abc import Sequence
from datetime import date
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from models.daily_activity import DailyActivity

COUNTERS = ("words_saved", "reviews", "words_read")


class ActivityRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def increment(self, user_id: UUID, day: date, counter: str, amount: int = 1) -> None:
        if counter not in COUNTERS:
            raise ValueError(counter)
        column = DailyActivity.__table__.c[counter]
        statement = (
            insert(DailyActivity)
            .values(user_id=user_id, day=day, **{counter: amount})
            .on_conflict_do_update(
                index_elements=[DailyActivity.user_id, DailyActivity.day],
                set_={counter: column + amount},
            )
        )
        await self._session.execute(statement)
        await self._session.commit()

    async def get_day(self, user_id: UUID, day: date) -> DailyActivity | None:
        return await self._session.get(DailyActivity, (user_id, day))

    async def list_recent(self, user_id: UUID, since: date) -> Sequence[DailyActivity]:
        result = await self._session.scalars(
            select(DailyActivity)
            .where(DailyActivity.user_id == user_id, DailyActivity.day >= since)
            .order_by(DailyActivity.day.desc())
        )
        return result.all()

    async def total_words_read(self, user_id: UUID) -> int:
        total = await self._session.scalar(
            select(func.coalesce(func.sum(DailyActivity.words_read), 0)).where(
                DailyActivity.user_id == user_id
            )
        )
        return int(total or 0)
