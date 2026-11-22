from uuid import UUID

from core.exceptions import LessonNotFoundError
from core.vocabulary import count_words
from models.lesson import Lesson
from repositories.lesson_repository import LessonRepository
from schemas.lesson import LessonCreate, LessonOut, LessonSummaryOut

PREVIEW_LENGTH = 160


class LessonService:
    def __init__(self, repository: LessonRepository) -> None:
        self._repository = repository

    async def list_lessons(self, user_id: UUID) -> list[LessonSummaryOut]:
        lessons = await self._repository.list_by_user(user_id)
        return [
            LessonSummaryOut(
                id=lesson.id,
                title=lesson.title,
                preview=" ".join(lesson.body.split())[:PREVIEW_LENGTH],
                word_count=count_words(lesson.body),
                created_at=lesson.created_at,
            )
            for lesson in lessons
        ]

    async def get_lesson(self, user_id: UUID, lesson_id: UUID) -> LessonOut:
        lesson = await self._repository.get(user_id, lesson_id)
        if lesson is None:
            raise LessonNotFoundError()
        return self._to_out(lesson)

    async def create_lesson(self, user_id: UUID, data: LessonCreate) -> LessonOut:
        lesson = await self._repository.add(
            {"user_id": user_id, "title": data.title, "body": data.body.strip()}
        )
        return self._to_out(lesson)

    async def delete_lesson(self, user_id: UUID, lesson_id: UUID) -> None:
        lesson = await self._repository.get(user_id, lesson_id)
        if lesson is None:
            raise LessonNotFoundError()
        await self._repository.delete(lesson)

    @staticmethod
    def _to_out(lesson: Lesson) -> LessonOut:
        return LessonOut(
            id=lesson.id,
            title=lesson.title,
            body=lesson.body,
            word_count=count_words(lesson.body),
            created_at=lesson.created_at,
        )
