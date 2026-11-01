from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.phrase import Phrase
from models.podcast_episode import PodcastEpisode


class ContentRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list_podcasts(self, language_id: UUID) -> Sequence[PodcastEpisode]:
        result = await self._session.scalars(
            select(PodcastEpisode)
            .where(PodcastEpisode.language_id == language_id)
            .order_by(PodcastEpisode.position)
        )
        return result.all()

    async def list_phrases(self, language_id: UUID) -> Sequence[Phrase]:
        result = await self._session.scalars(
            select(Phrase)
            .where(Phrase.language_id == language_id)
            .order_by(Phrase.kind, Phrase.position)
        )
        return result.all()
