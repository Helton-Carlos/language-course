from fastapi import APIRouter, status

from routes.dependencies import CurrentUserDep, StatsServiceDep
from schemas.stats import ReadingActivityIn, StatsOut

stats_routes = APIRouter(prefix="/stats", tags=["Stats"])


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
