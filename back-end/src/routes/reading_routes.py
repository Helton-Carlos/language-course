from fastapi import APIRouter

from routes.dependencies import CurrentUserDep, ReadingServiceDep
from schemas.reading import ReadingSituationOut, ReadingTextOut, ReadingThemeOut

reading_routes = APIRouter(prefix="/reading", tags=["Reading"])


@reading_routes.get("/themes", response_model=list[ReadingThemeOut])
async def list_themes(_: CurrentUserDep, service: ReadingServiceDep) -> list[ReadingThemeOut]:
    return service.list_themes()


@reading_routes.get("/themes/{theme}/situations", response_model=list[ReadingSituationOut])
async def list_situations(
    theme: str,
    _: CurrentUserDep,
    service: ReadingServiceDep,
) -> list[ReadingSituationOut]:
    return service.list_situations(theme)


@reading_routes.get("/themes/{theme}/situations/{situation}", response_model=ReadingTextOut)
async def get_text(
    theme: str,
    situation: str,
    current_user: CurrentUserDep,
    service: ReadingServiceDep,
) -> ReadingTextOut:
    return await service.get_text(theme, situation, current_user.level)
