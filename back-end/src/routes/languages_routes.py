from fastapi import APIRouter

from core.english import ENGLISH
from schemas.language import LanguageOut

languages_routes = APIRouter(tags=["Languages"])


@languages_routes.get("/languages", response_model=list[LanguageOut])
async def list_languages() -> list[dict]:
    return [ENGLISH]
