from uuid import UUID

from core.exceptions import LanguageNotFoundError
from repositories.content_repository import ContentRepository
from repositories.language_repository import LanguageRepository
from schemas.content import PhraseOut, PodcastEpisodeOut


class ContentService:
    def __init__(
        self,
        content_repository: ContentRepository,
        language_repository: LanguageRepository,
    ) -> None:
        self._content_repository = content_repository
        self._language_repository = language_repository

    async def list_podcasts(self, language_id: UUID) -> list[PodcastEpisodeOut]:
        await self._ensure_language(language_id)
        episodes = await self._content_repository.list_podcasts(language_id)
        return [PodcastEpisodeOut.model_validate(episode) for episode in episodes]

    async def list_phrases(self, language_id: UUID) -> list[PhraseOut]:
        await self._ensure_language(language_id)
        phrases = await self._content_repository.list_phrases(language_id)
        return [PhraseOut.model_validate(phrase) for phrase in phrases]

    async def _ensure_language(self, language_id: UUID) -> None:
        if await self._language_repository.get(language_id) is None:
            raise LanguageNotFoundError()
