import uuid

from sqlalchemy import CheckConstraint, String, Text, UniqueConstraint, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class ReadingText(Base):
    __tablename__ = "reading_texts"
    __table_args__ = (
        CheckConstraint("band IN ('A1-A2', 'B1-B2', 'C1-C2')", name="band_valid"),
        UniqueConstraint("theme", "situation", "band", name="uq_reading_texts_theme_situation_band"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
    theme: Mapped[str] = mapped_column(String(30))
    situation: Mapped[str] = mapped_column(String(40))
    band: Mapped[str] = mapped_column(String(5))
    title: Mapped[str] = mapped_column(String(200))
    body: Mapped[str] = mapped_column(Text)
