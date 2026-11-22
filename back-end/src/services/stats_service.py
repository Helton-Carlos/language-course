from datetime import date, timedelta
from uuid import UUID

from core.vocabulary import (
    DAILY_GOAL,
    KNOWN_STATUS,
    STREAK_LOOKBACK_DAYS,
    now_utc,
    today_local,
)
from repositories.activity_repository import ActivityRepository
from repositories.vocabulary_repository import VocabularyRepository
from schemas.stats import DayActivityOut, StatsOut, StatusCountOut

LAST_DAYS = 7


class StatsService:
    def __init__(
        self,
        vocabulary_repository: VocabularyRepository,
        activity_repository: ActivityRepository,
    ) -> None:
        self._vocabulary_repository = vocabulary_repository
        self._activity_repository = activity_repository

    async def get_stats(self, user_id: UUID) -> StatsOut:
        today = today_local()
        counts = await self._vocabulary_repository.count_by_status(user_id)
        due_count = await self._vocabulary_repository.count_due(user_id, now_utc())
        words_read_total = await self._activity_repository.total_words_read(user_id)
        rows = await self._activity_repository.list_recent(
            user_id, today - timedelta(days=STREAK_LOOKBACK_DAYS)
        )
        by_day = {row.day: row for row in rows}
        today_row = by_day.get(today)
        today_out = DayActivityOut(
            day=today,
            words_saved=today_row.words_saved if today_row else 0,
            reviews=today_row.reviews if today_row else 0,
            words_read=today_row.words_read if today_row else 0,
        )
        last_days = [
            self._day_out(by_day, today - timedelta(days=offset))
            for offset in range(LAST_DAYS - 1, -1, -1)
        ]
        return StatsOut(
            daily_goal=DAILY_GOAL,
            today=today_out,
            today_progress=today_out.words_saved + today_out.reviews,
            streak=self._streak(by_day, today),
            known_words=counts.get(KNOWN_STATUS, 0),
            total_items=sum(counts.values()),
            due_count=due_count,
            words_read_total=words_read_total,
            by_status=[StatusCountOut(status=status, count=counts.get(status, 0)) for status in range(1, 6)],
            last_days=last_days,
        )

    async def record_reading(self, user_id: UUID, words: int) -> None:
        await self._activity_repository.increment(user_id, today_local(), "words_read", words)

    @staticmethod
    def _day_out(by_day: dict, day: date) -> DayActivityOut:
        row = by_day.get(day)
        return DayActivityOut(
            day=day,
            words_saved=row.words_saved if row else 0,
            reviews=row.reviews if row else 0,
            words_read=row.words_read if row else 0,
        )

    @staticmethod
    def _streak(by_day: dict, today: date) -> int:
        def active(day: date) -> bool:
            row = by_day.get(day)
            return row is not None and (row.words_saved + row.reviews + row.words_read) > 0

        cursor = today if active(today) else today - timedelta(days=1)
        streak = 0
        while active(cursor):
            streak += 1
            cursor -= timedelta(days=1)
        return streak
