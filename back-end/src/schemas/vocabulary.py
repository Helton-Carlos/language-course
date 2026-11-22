import re
from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import AfterValidator, Field

from core.vocabulary import normalize_term
from schemas.base import APIModel

MAX_TERM_LENGTH = 100
MAX_BULK_TERMS = 3000


def _validate_term(value: str) -> str:
    term = normalize_term(value)
    if not term or len(term) > MAX_TERM_LENGTH or not re.search(r"[a-z]", term):
        raise ValueError("Informe uma palavra ou frase em inglês com até 100 caracteres")
    return term


Term = Annotated[str, AfterValidator(_validate_term)]
Status = Annotated[int, Field(ge=1, le=5)]
Meaning = Annotated[str, Field(max_length=300)]
Context = Annotated[str, Field(max_length=1000)]


class VocabularyCreate(APIModel):
    term: Term
    meaning: Meaning = ""
    context: Context | None = None
    status: Status = 1


class VocabularyUpdate(APIModel):
    meaning: Meaning | None = None
    context: Context | None = None
    status: Status | None = None


class VocabularyKnownBulk(APIModel):
    terms: Annotated[list[Term], Field(min_length=1, max_length=MAX_BULK_TERMS)]


class VocabularyKnownBulkOut(APIModel):
    created: int


class VocabularyReviewAnswer(APIModel):
    correct: bool


class VocabularyOut(APIModel):
    id: UUID
    term: str
    meaning: str
    context: str | None = None
    status: int
    review_count: int
    next_review_at: datetime | None = None
    created_at: datetime
    updated_at: datetime


class VocabularyMapOut(APIModel):
    term: str
    meaning: str
    status: int
