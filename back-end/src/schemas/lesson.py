from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import Field

from schemas.base import APIModel

MAX_LESSON_LENGTH = 60000


class LessonCreate(APIModel):
    title: Annotated[str, Field(min_length=1, max_length=200)]
    body: Annotated[str, Field(min_length=1, max_length=MAX_LESSON_LENGTH)]


class LessonSummaryOut(APIModel):
    id: UUID
    title: str
    preview: str
    word_count: int
    created_at: datetime


class LessonOut(APIModel):
    id: UUID
    title: str
    body: str
    word_count: int
    created_at: datetime
