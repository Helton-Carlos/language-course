import uuid

from sqlalchemy import CheckConstraint, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.language import Language


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint("role IN ('admin', 'user')", name="role_valid"),
        CheckConstraint(
            "level IS NULL OR level IN ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')",
            name="level_valid",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
    name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    role: Mapped[str] = mapped_column(String(20), server_default="user")
    password_hash: Mapped[str] = mapped_column(String(255))
    language_id: Mapped[uuid.UUID | None] = mapped_column(
        Uuid,
        ForeignKey("languages.id", ondelete="SET NULL"),
    )
    level: Mapped[str | None] = mapped_column(String(2))

    language: Mapped[Language | None] = relationship(lazy="joined")
