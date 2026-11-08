from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from core.database import SessionDep
from repositories.content_repository import ContentRepository
from routes.dependencies import CurrentUserDep
from schemas.content import PhraseOut, PodcastEpisodeOut
from services.content_service import ContentService

content_routes = APIRouter(tags=["Content"])


def get_content_service(session: SessionDep) -> ContentService:
    return ContentService(ContentRepository(session))


ContentServiceDep = Annotated[ContentService, Depends(get_content_service)]


@content_routes.get("/languages/{language_id}/podcasts", response_model=list[PodcastEpisodeOut])
async def list_podcasts(
    language_id: UUID,
    _: CurrentUserDep,
    service: ContentServiceDep,
) -> list[PodcastEpisodeOut]:
    return await service.list_podcasts(language_id)


@content_routes.get("/languages/{language_id}/phrases", response_model=list[PhraseOut])
async def list_phrases(
    language_id: UUID,
    _: CurrentUserDep,
    service: ContentServiceDep,
) -> list[PhraseOut]:
    return await service.list_phrases(language_id)
