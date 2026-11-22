from typing import Annotated

from fastapi import APIRouter, Depends, status

from core.database import SessionDep
from repositories.activity_repository import ActivityRepository
from repositories.vocabulary_repository import VocabularyRepository
from routes.dependencies import CurrentUserDep
from schemas.stats import ReadingActivityIn, StatsOut
from services.stats_service import StatsService

stats_routes = APIRouter(prefix="/stats", tags=["Stats"])


def get_stats_service(session: SessionDep) -> StatsService:
    return StatsService(VocabularyRepository(session), ActivityRepository(session))


StatsServiceDep = Annotated[StatsService, Depends(get_stats_service)]


@stats_routes.get("", response_model=StatsOut)
async def get_stats(current_user: CurrentUserDep, service: StatsServiceDep) -> StatsOut:
    return await service.get_stats(current_user.id)


@stats_routes.post("/reading", status_code=status.HTTP_204_NO_CONTENT)
async def record_reading(
    data: ReadingActivityIn,
    current_user: CurrentUserDep,
    service: StatsServiceDep,
) -> None:
    await service.record_reading(current_user.id, data.words)
