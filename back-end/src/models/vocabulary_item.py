import uuid
from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    SmallInteger,
    String,
    Text,
    UniqueConstraint,
    Uuid,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class VocabularyItem(Base):
    __tablename__ = "vocabulary_items"
    __table_args__ = (
        CheckConstraint("status BETWEEN 1 AND 5", name="status_valid"),
        UniqueConstraint("user_id", "term", name="uq_vocabulary_items_user_id_term"),
        Index("ix_vocabulary_items_user_id_status", "user_id", "status"),
        Index("ix_vocabulary_items_user_id_next_review_at", "user_id", "next_review_at"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("users.id", ondelete="CASCADE"))
    term: Mapped[str] = mapped_column(String(100))
    meaning: Mapped[str] = mapped_column(String(300), server_default="")
    context: Mapped[str | None] = mapped_column(Text)
    status: Mapped[int] = mapped_column(SmallInteger, server_default="1")
    review_count: Mapped[int] = mapped_column(SmallInteger, server_default="0")
    next_review_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
