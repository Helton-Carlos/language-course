from uuid import UUID

from fastapi import APIRouter

from routes.dependencies import ContentServiceDep, CurrentUserDep
from schemas.content import PhraseOut, PodcastEpisodeOut

content_routes = APIRouter(tags=["Content"])


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
