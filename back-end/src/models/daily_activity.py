import uuid
from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class DailyActivity(Base):
    __tablename__ = "daily_activities"

    user_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    day: Mapped[date] = mapped_column(Date, primary_key=True)
    words_saved: Mapped[int] = mapped_column(Integer, server_default="0")
    reviews: Mapped[int] = mapped_column(Integer, server_default="0")
    words_read: Mapped[int] = mapped_column(Integer, server_default="0")
