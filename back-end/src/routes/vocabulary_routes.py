from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Query, Response, status

from core.database import SessionDep
from repositories.activity_repository import ActivityRepository
from repositories.vocabulary_repository import VocabularyRepository
from routes.dependencies import CurrentUserDep
from schemas.vocabulary import (
    VocabularyCreate,
    VocabularyKnownBulk,
    VocabularyKnownBulkOut,
    VocabularyMapOut,
    VocabularyOut,
    VocabularyReviewAnswer,
    VocabularyUpdate,
)
from services.vocabulary_service import VocabularyService

vocabulary_routes = APIRouter(prefix="/vocabulary", tags=["Vocabulary"])


def get_vocabulary_service(session: SessionDep) -> VocabularyService:
    return VocabularyService(VocabularyRepository(session), ActivityRepository(session))


VocabularyServiceDep = Annotated[VocabularyService, Depends(get_vocabulary_service)]


@vocabulary_routes.get("", response_model=list[VocabularyOut])
async def list_items(
    current_user: CurrentUserDep,
    service: VocabularyServiceDep,
    item_status: Annotated[int | None, Query(alias="status", ge=1, le=5)] = None,
    search: Annotated[str | None, Query(max_length=100)] = None,
    limit: Annotated[int, Query(ge=1, le=200)] = 50,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> list[VocabularyOut]:
    return await service.list_items(current_user.id, item_status, search, limit, offset)


@vocabulary_routes.get("/map", response_model=list[VocabularyMapOut])
async def list_map(current_user: CurrentUserDep, service: VocabularyServiceDep) -> list[VocabularyMapOut]:
    return await service.list_map(current_user.id)


@vocabulary_routes.get("/review", response_model=list[VocabularyOut])
async def list_due(current_user: CurrentUserDep, service: VocabularyServiceDep) -> list[VocabularyOut]:
    return await service.list_due(current_user.id)


@vocabulary_routes.post("/known", response_model=VocabularyKnownBulkOut)
async def mark_known(
    data: VocabularyKnownBulk,
    current_user: CurrentUserDep,
    service: VocabularyServiceDep,
) -> VocabularyKnownBulkOut:
    return await service.mark_known(current_user.id, data)


@vocabulary_routes.post("", response_model=VocabularyOut, status_code=status.HTTP_201_CREATED)
async def save_item(
    data: VocabularyCreate,
    response: Response,
    current_user: CurrentUserDep,
    service: VocabularyServiceDep,
) -> VocabularyOut:
    item, created = await service.save(current_user.id, data)
    if not created:
        response.status_code = status.HTTP_200_OK
    return item


@vocabulary_routes.post("/{item_id}/review", response_model=VocabularyOut)
async def answer_review(
    item_id: UUID,
    data: VocabularyReviewAnswer,
    current_user: CurrentUserDep,
    service: VocabularyServiceDep,
) -> VocabularyOut:
    return await service.answer_review(current_user.id, item_id, data.correct)


@vocabulary_routes.patch("/{item_id}", response_model=VocabularyOut)
async def update_item(
    item_id: UUID,
    data: VocabularyUpdate,
    current_user: CurrentUserDep,
    service: VocabularyServiceDep,
) -> VocabularyOut:
    return await service.update(current_user.id, item_id, data)


@vocabulary_routes.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item_id: UUID,
    current_user: CurrentUserDep,
    service: VocabularyServiceDep,
) -> None:
    await service.delete(current_user.id, item_id)
