from typing import Literal
from uuid import UUID

from schemas.base import APIModel

PhraseKind = Literal["phrase", "slang"]


class PodcastEpisodeOut(APIModel):
    id: UUID
    title: str
    youtube_id: str


class PhraseOut(APIModel):
    id: UUID
    kind: PhraseKind
    text: str
    translation: str
