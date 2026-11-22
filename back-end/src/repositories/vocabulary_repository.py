from collections.abc import Sequence
from datetime import datetime
from typing import Any
from uuid import UUID

from sqlalchemy import func, or_, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from core.vocabulary import KNOWN_STATUS
from models.vocabulary_item import VocabularyItem


class VocabularyRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list_items(
        self,
        user_id: UUID,
        status: int | None,
        search: str | None,
        limit: int,
        offset: int,
    ) -> Sequence[VocabularyItem]:
        statement = select(VocabularyItem).where(VocabularyItem.user_id == user_id)
        if status is not None:
            statement = statement.where(VocabularyItem.status == status)
        if search:
            pattern = f"%{_escape_like(search.lower())}%"
            statement = statement.where(
                or_(
                    VocabularyItem.term.like(pattern, escape="\\"),
                    func.lower(VocabularyItem.meaning).like(pattern, escape="\\"),
                )
            )
        statement = statement.order_by(VocabularyItem.updated_at.desc(), VocabularyItem.term)
        result = await self._session.scalars(statement.limit(limit).offset(offset))
        return result.all()

    async def list_all(self, user_id: UUID) -> Sequence[VocabularyItem]:
        result = await self._session.scalars(
            select(VocabularyItem).where(VocabularyItem.user_id == user_id)
        )
        return result.all()

    async def get(self, user_id: UUID, item_id: UUID) -> VocabularyItem | None:
        return await self._session.scalar(
            select(VocabularyItem).where(
                VocabularyItem.user_id == user_id,
                VocabularyItem.id == item_id,
            )
        )

    async def get_by_term(self, user_id: UUID, term: str) -> VocabularyItem | None:
        return await self._session.scalar(
            select(VocabularyItem).where(
                VocabularyItem.user_id == user_id,
                VocabularyItem.term == term,
            )
        )

    async def add(self, values: dict[str, Any]) -> VocabularyItem:
        item = VocabularyItem(**values)
        self._session.add(item)
        await self._session.commit()
        await self._session.refresh(item)
        return item

    async def update(self, item: VocabularyItem, values: dict[str, Any]) -> VocabularyItem:
        for field, value in values.items():
            setattr(item, field, value)
        await self._session.commit()
        await self._session.refresh(item)
        return item

    async def delete(self, item: VocabularyItem) -> None:
        await self._session.delete(item)
        await self._session.commit()

    async def list_due(self, user_id: UUID, moment: datetime, limit: int) -> Sequence[VocabularyItem]:
        result = await self._session.scalars(
            select(VocabularyItem)
            .where(
                VocabularyItem.user_id == user_id,
                VocabularyItem.status < KNOWN_STATUS,
                VocabularyItem.next_review_at <= moment,
                VocabularyItem.meaning != "",
            )
            .order_by(VocabularyItem.next_review_at)
            .limit(limit)
        )
        return result.all()

    async def count_due(self, user_id: UUID, moment: datetime) -> int:
        total = await self._session.scalar(
            select(func.count())
            .select_from(VocabularyItem)
            .where(
                VocabularyItem.user_id == user_id,
                VocabularyItem.status < KNOWN_STATUS,
                VocabularyItem.next_review_at <= moment,
                VocabularyItem.meaning != "",
            )
        )
        return total or 0

    async def count_by_status(self, user_id: UUID) -> dict[int, int]:
        rows = await self._session.execute(
            select(VocabularyItem.status, func.count())
            .where(VocabularyItem.user_id == user_id)
            .group_by(VocabularyItem.status)
        )
        return {status: count for status, count in rows.all()}

    async def add_known_bulk(self, user_id: UUID, terms: Sequence[str]) -> int:
        statement = (
            insert(VocabularyItem)
            .values([{"user_id": user_id, "term": term, "status": KNOWN_STATUS} for term in terms])
            .on_conflict_do_nothing(constraint="uq_vocabulary_items_user_id_term")
            .returning(VocabularyItem.id)
        )
        result = await self._session.execute(statement)
        created = len(result.all())
        await self._session.commit()
        return created


def _escape_like(value: str) -> str:
    return value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
