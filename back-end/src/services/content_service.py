from uuid import UUID

from core.english import ensure_english
from repositories.content_repository import ContentRepository
from schemas.content import PhraseOut, PodcastEpisodeOut


class ContentService:
    def __init__(self, content_repository: ContentRepository) -> None:
        self._content_repository = content_repository

    async def list_podcasts(self, language_id: UUID) -> list[PodcastEpisodeOut]:
        ensure_english(language_id)
        episodes = await self._content_repository.list_podcasts(language_id)
        return [PodcastEpisodeOut.model_validate(episode) for episode in episodes]

    async def list_phrases(self, language_id: UUID) -> list[PhraseOut]:
        ensure_english(language_id)
        phrases = await self._content_repository.list_phrases(language_id)
        return [PhraseOut.model_validate(phrase) for phrase in phrases]
