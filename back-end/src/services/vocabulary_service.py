from uuid import UUID

from core.exceptions import VocabularyItemNotFoundError
from core.vocabulary import (
    KNOWN_STATUS,
    MIN_STATUS,
    REVIEW_BATCH_SIZE,
    next_review_for,
    now_utc,
    today_local,
)
from repositories.activity_repository import ActivityRepository
from repositories.vocabulary_repository import VocabularyRepository
from schemas.vocabulary import (
    VocabularyCreate,
    VocabularyKnownBulk,
    VocabularyKnownBulkOut,
    VocabularyMapOut,
    VocabularyOut,
    VocabularyUpdate,
)


class VocabularyService:
    def __init__(
        self,
        repository: VocabularyRepository,
        activity_repository: ActivityRepository,
    ) -> None:
        self._repository = repository
        self._activity_repository = activity_repository

    async def list_items(
        self,
        user_id: UUID,
        status: int | None,
        search: str | None,
        limit: int,
        offset: int,
    ) -> list[VocabularyOut]:
        items = await self._repository.list_items(user_id, status, search, limit, offset)
        return [VocabularyOut.model_validate(item) for item in items]

    async def list_map(self, user_id: UUID) -> list[VocabularyMapOut]:
        items = await self._repository.list_all(user_id)
        return [VocabularyMapOut.model_validate(item) for item in items]

    async def save(self, user_id: UUID, data: VocabularyCreate) -> tuple[VocabularyOut, bool]:
        existing = await self._repository.get_by_term(user_id, data.term)
        if existing is not None:
            values = {"meaning": data.meaning, "status": data.status}
            if data.context is not None:
                values["context"] = data.context
            values["next_review_at"] = self._schedule_after_edit(existing.next_review_at, data.status)
            updated = await self._repository.update(existing, values)
            return VocabularyOut.model_validate(updated), False
        moment = now_utc()
        created = await self._repository.add(
            {
                "user_id": user_id,
                "term": data.term,
                "meaning": data.meaning,
                "context": data.context,
                "status": data.status,
                "next_review_at": None if data.status == KNOWN_STATUS else moment,
            }
        )
        await self._activity_repository.increment(user_id, today_local(), "lingqs_created")
        return VocabularyOut.model_validate(created), True

    async def update(self, user_id: UUID, item_id: UUID, data: VocabularyUpdate) -> VocabularyOut:
        item = await self._repository.get(user_id, item_id)
        if item is None:
            raise VocabularyItemNotFoundError()
        values = data.model_dump(exclude_unset=True, exclude_none=True)
        if "status" in values:
            values["next_review_at"] = self._schedule_after_edit(item.next_review_at, values["status"])
        updated = await self._repository.update(item, values)
        return VocabularyOut.model_validate(updated)

    async def delete(self, user_id: UUID, item_id: UUID) -> None:
        item = await self._repository.get(user_id, item_id)
        if item is None:
            raise VocabularyItemNotFoundError()
        await self._repository.delete(item)

    async def list_due(self, user_id: UUID) -> list[VocabularyOut]:
        items = await self._repository.list_due(user_id, now_utc(), REVIEW_BATCH_SIZE)
        return [VocabularyOut.model_validate(item) for item in items]

    async def answer_review(self, user_id: UUID, item_id: UUID, correct: bool) -> VocabularyOut:
        item = await self._repository.get(user_id, item_id)
        if item is None:
            raise VocabularyItemNotFoundError()
        status = min(KNOWN_STATUS, item.status + 1) if correct else max(MIN_STATUS, item.status - 1)
        updated = await self._repository.update(
            item,
            {
                "status": status,
                "review_count": item.review_count + 1,
                "next_review_at": next_review_for(status, now_utc()),
            },
        )
        await self._activity_repository.increment(user_id, today_local(), "reviews")
        return VocabularyOut.model_validate(updated)

    async def mark_known(self, user_id: UUID, data: VocabularyKnownBulk) -> VocabularyKnownBulkOut:
        terms = list(dict.fromkeys(data.terms))
        created = await self._repository.add_known_bulk(user_id, terms)
        return VocabularyKnownBulkOut(created=created)

    @staticmethod
    def _schedule_after_edit(current, status: int):
        if status == KNOWN_STATUS:
            return None
        return current or now_utc()
