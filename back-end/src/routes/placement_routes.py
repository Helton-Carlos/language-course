from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from core.database import SessionDep
from repositories.language_repository import LanguageRepository
from repositories.placement_repository import PlacementRepository
from routes.dependencies import CurrentUserDep
from schemas.level import Level
from schemas.placement import PlacementResultOut, PlacementSubmission, PlacementTestOut
from services.placement_service import PlacementService

placement_routes = APIRouter(tags=["Placement"])


def get_placement_service(session: SessionDep) -> PlacementService:
    return PlacementService(PlacementRepository(session), LanguageRepository(session))


PlacementServiceDep = Annotated[PlacementService, Depends(get_placement_service)]


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
