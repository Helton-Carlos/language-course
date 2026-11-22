from uuid import UUID

from fastapi import APIRouter, status

from routes.dependencies import CurrentUserDep, LessonServiceDep
from schemas.lesson import LessonCreate, LessonOut, LessonSummaryOut

lessons_routes = APIRouter(prefix="/lessons", tags=["Lessons"])


@lessons_routes.get("", response_model=list[LessonSummaryOut])
async def list_lessons(
    current_user: CurrentUserDep, service: LessonServiceDep
) -> list[LessonSummaryOut]:
    return await service.list_lessons(current_user.id)


@lessons_routes.post("", response_model=LessonOut, status_code=status.HTTP_201_CREATED)
async def create_lesson(
    data: LessonCreate,
    current_user: CurrentUserDep,
    service: LessonServiceDep,
) -> LessonOut:
    return await service.create_lesson(current_user.id, data)


@lessons_routes.get("/{lesson_id}", response_model=LessonOut)
async def get_lesson(
    lesson_id: UUID,
    current_user: CurrentUserDep,
    service: LessonServiceDep,
) -> LessonOut:
    return await service.get_lesson(current_user.id, lesson_id)


@lessons_routes.delete("/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lesson(
    lesson_id: UUID,
    current_user: CurrentUserDep,
    service: LessonServiceDep,
) -> None:
    await service.delete_lesson(current_user.id, lesson_id)
