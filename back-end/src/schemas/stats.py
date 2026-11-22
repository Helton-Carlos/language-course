from datetime import date
from typing import Annotated

from pydantic import Field

from schemas.base import APIModel


class ReadingActivityIn(APIModel):
    words: Annotated[int, Field(ge=1, le=100000)]


class DayActivityOut(APIModel):
    day: date
    words_saved: int
    reviews: int
    words_read: int


class StatusCountOut(APIModel):
    status: int
    count: int


class StatsOut(APIModel):
    daily_goal: int
    today: DayActivityOut
    today_progress: int
    streak: int
    known_words: int
    total_items: int
    due_count: int
    words_read_total: int
    by_status: list[StatusCountOut]
    last_days: list[DayActivityOut]
