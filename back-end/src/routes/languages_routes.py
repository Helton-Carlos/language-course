from fastapi import APIRouter

from utils.languages import LANGUAGES

languages_routes = APIRouter(tags=['Languages'])

@languages_routes.get("/languages")
async def get_languages() -> list[dict[str, str]]:
    return LANGUAGES