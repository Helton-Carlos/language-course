from uuid import UUID

from pydantic import Field

from schemas.base import APIModel
from schemas.level import Level


class PlacementOptionOut(APIModel):
    index: int
    text: str


class PlacementQuestionOut(APIModel):
    id: UUID
    prompt: str
    options: list[PlacementOptionOut]


class PlacementTestOut(APIModel):
    level: Level
    questions: list[PlacementQuestionOut]


class PlacementAnswer(APIModel):
    question_id: UUID
    option_index: int = Field(ge=0, le=3)


class PlacementSubmission(APIModel):
    answers: list[PlacementAnswer] = Field(min_length=1, max_length=10)


class PlacementResultOut(APIModel):
    level: Level
    correct: int
    total: int
    passed: bool
    next_level: Level | None = None
    result_level: Level | None = None
