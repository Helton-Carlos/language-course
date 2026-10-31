from typing import Annotated

from fastapi import APIRouter, Depends

from repositories.language_repository import LanguageRepository
from schemas.language import LanguageOut
from services.language_service import LanguageService

languages_routes = APIRouter(tags=["Languages"])


def get_language_service() -> LanguageService:
    return LanguageService(LanguageRepository())


LanguageServiceDep = Annotated[LanguageService, Depends(get_language_service)]


@languages_routes.get("/languages", response_model=list[LanguageOut])
async def get_languages(service: LanguageServiceDep) -> list[LanguageOut]:
    return service.list_languages()
