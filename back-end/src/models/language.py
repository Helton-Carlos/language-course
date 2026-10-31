import uuid

from sqlalchemy import String, Text, Uuid, func, text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Language(Base):
    __tablename__ = "languages"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
    code: Mapped[str] = mapped_column(String(10), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    name_pt: Mapped[str] = mapped_column(String(100))
    prefix: Mapped[str] = mapped_column(String(2))
    description: Mapped[str] = mapped_column(Text)
    countries: Mapped[list[str]] = mapped_column(
        ARRAY(String(100)),
        server_default=text("'{}'"),
    )
