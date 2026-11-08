import uuid

from sqlalchemy import CheckConstraint, Index, SmallInteger, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class PodcastEpisode(Base):
    __tablename__ = "podcast_episodes"
    __table_args__ = (
        CheckConstraint("youtube_id ~ '^[A-Za-z0-9_-]{11}$'", name="youtube_id_valid"),
        Index("ix_podcast_episodes_language_id_position", "language_id", "position"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
    language_id: Mapped[uuid.UUID] = mapped_column(Uuid)
    title: Mapped[str] = mapped_column(String(200))
    youtube_id: Mapped[str] = mapped_column(String(11))
    position: Mapped[int] = mapped_column(SmallInteger, server_default="0")
