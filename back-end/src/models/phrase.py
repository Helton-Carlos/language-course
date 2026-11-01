import uuid

from sqlalchemy import CheckConstraint, ForeignKey, Index, SmallInteger, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Phrase(Base):
    __tablename__ = "phrases"
    __table_args__ = (
        CheckConstraint("kind IN ('phrase', 'slang')", name="kind_valid"),
        Index("ix_phrases_language_id_position", "language_id", "position"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
    language_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("languages.id", ondelete="CASCADE"),
    )
    kind: Mapped[str] = mapped_column(String(10))
    text: Mapped[str] = mapped_column(String(300))
    translation: Mapped[str] = mapped_column(String(300))
    position: Mapped[int] = mapped_column(SmallInteger, server_default="0")
