import uuid

from sqlalchemy import CheckConstraint, Index, SmallInteger, String, Text, Uuid, func
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class PlacementQuestion(Base):
    __tablename__ = "placement_questions"
    __table_args__ = (
        CheckConstraint("level IN ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')", name="level_valid"),
        CheckConstraint("cardinality(options) = 4", name="four_options"),
        CheckConstraint("correct_index >= 0 AND correct_index < 4", name="correct_index_valid"),
        Index("ix_placement_questions_language_id_level", "language_id", "level"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
    language_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    level: Mapped[str] = mapped_column(String(2))
    prompt: Mapped[str] = mapped_column(Text)
    options: Mapped[list[str]] = mapped_column(ARRAY(Text))
    correct_index: Mapped[int] = mapped_column(SmallInteger)
