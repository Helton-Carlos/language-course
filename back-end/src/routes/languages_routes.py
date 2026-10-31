from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Response, status

from core.database import SessionDep
from repositories.language_repository import LanguageRepository
from schemas.language import LanguageCreate, LanguageOut, LanguageUpdate
from services.language_service import LanguageService

languages_routes = APIRouter(tags=["Languages"])


def get_language_service(session: SessionDep) -> LanguageService:
    return LanguageService(LanguageRepository(session))


LanguageServiceDep = Annotated[LanguageService, Depends(get_language_service)]


@languages_routes.get("/languages", response_model=list[LanguageOut])
async def list_languages(service: LanguageServiceDep) -> list[LanguageOut]:
    return await service.list_languages()


@languages_routes.get("/languages/{language_id}", response_model=LanguageOut)
async def get_language(language_id: UUID, service: LanguageServiceDep) -> LanguageOut:
    return await service.get_language(language_id)


@languages_routes.post(
    "/languages",
    response_model=LanguageOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_language(data: LanguageCreate, service: LanguageServiceDep) -> LanguageOut:
    return await service.create_language(data)


@languages_routes.patch("/languages/{language_id}", response_model=LanguageOut)
async def update_language(
    language_id: UUID,
    data: LanguageUpdate,
    service: LanguageServiceDep,
) -> LanguageOut:
    return await service.update_language(language_id, data)


@languages_routes.delete("/languages/{language_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_language(language_id: UUID, service: LanguageServiceDep) -> Response:
    await service.delete_language(language_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
