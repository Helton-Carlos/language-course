import random
from uuid import UUID

from core.exceptions import (
    InvalidPlacementAnswersError,
    LanguageNotFoundError,
    PlacementTestUnavailableError,
)
from repositories.language_repository import LanguageRepository
from repositories.placement_repository import PlacementRepository
from schemas.level import LEVELS, Level
from schemas.placement import (
    PlacementOptionOut,
    PlacementQuestionOut,
    PlacementResultOut,
    PlacementSubmission,
    PlacementTestOut,
)

PASS_NUMERATOR = 2
PASS_DENOMINATOR = 3


class PlacementService:
    def __init__(
        self,
        placement_repository: PlacementRepository,
        language_repository: LanguageRepository,
    ) -> None:
        self._placement_repository = placement_repository
        self._language_repository = language_repository

    async def get_test(self, language_id: UUID, level: Level) -> PlacementTestOut:
        await self._ensure_language(language_id)

        questions = list(await self._placement_repository.list_by_level(language_id, level))
        if not questions:
            raise PlacementTestUnavailableError()

        random.shuffle(questions)

        return PlacementTestOut(
            level=level,
            questions=[
                PlacementQuestionOut(
                    id=question.id,
                    prompt=question.prompt,
                    options=self._shuffled_options(question.options),
                )
                for question in questions
            ],
        )

    async def submit(
        self,
        language_id: UUID,
        level: Level,
        submission: PlacementSubmission,
    ) -> PlacementResultOut:
        await self._ensure_language(language_id)

        questions = await self._placement_repository.list_by_level(language_id, level)
        if not questions:
            raise PlacementTestUnavailableError()

        by_id = {question.id: question for question in questions}
        answers = {answer.question_id: answer.option_index for answer in submission.answers}

        if len(answers) != len(submission.answers) or set(answers) != set(by_id):
            raise InvalidPlacementAnswersError()

        correct = sum(
            1 for question_id, index in answers.items()
            if by_id[question_id].correct_index == index
        )
        total = len(by_id)
        passed = correct * PASS_DENOMINATOR >= total * PASS_NUMERATOR

        position = LEVELS.index(level)
        next_level: Level | None = None
        result_level: Level | None = None

        if passed:
            candidate = LEVELS[position + 1] if position + 1 < len(LEVELS) else None
            if candidate is not None and await self._placement_repository.has_questions(
                language_id, candidate
            ):
                next_level = candidate
            else:
                result_level = level
        else:
            result_level = LEVELS[max(position - 1, 0)]

        return PlacementResultOut(
            level=level,
            correct=correct,
            total=total,
            passed=passed,
            next_level=next_level,
            result_level=result_level,
        )

    async def _ensure_language(self, language_id: UUID) -> None:
        if await self._language_repository.get(language_id) is None:
            raise LanguageNotFoundError()

    @staticmethod
    def _shuffled_options(options: list[str]) -> list[PlacementOptionOut]:
        indexed = list(enumerate(options))
        random.shuffle(indexed)
        return [PlacementOptionOut(index=index, text=text) for index, text in indexed]
