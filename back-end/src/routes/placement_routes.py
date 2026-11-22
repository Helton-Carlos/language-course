from uuid import UUID

from fastapi import APIRouter

from routes.dependencies import CurrentUserDep, PlacementServiceDep
from schemas.level import Level
from schemas.placement import PlacementResultOut, PlacementSubmission, PlacementTestOut

placement_routes = APIRouter(tags=["Placement"])


@placement_routes.get(
    "/languages/{language_id}/placement-test/{level}",
    response_model=PlacementTestOut,
)
async def get_placement_test(
    language_id: UUID,
    level: Level,
    _: CurrentUserDep,
    service: PlacementServiceDep,
) -> PlacementTestOut:
    return await service.get_test(language_id, level)


@placement_routes.post(
    "/languages/{language_id}/placement-test/{level}",
    response_model=PlacementResultOut,
)
async def submit_placement_test(
    language_id: UUID,
    level: Level,
    submission: PlacementSubmission,
    _: CurrentUserDep,
    service: PlacementServiceDep,
) -> PlacementResultOut:
    return await service.submit(language_id, level, submission)
