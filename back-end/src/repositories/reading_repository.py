from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.reading_text import ReadingText


class ReadingRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get(self, theme: str, situation: str, band: str) -> ReadingText | None:
        return await self._session.scalar(
            select(ReadingText).where(
                ReadingText.theme == theme,
                ReadingText.situation == situation,
                ReadingText.band == band,
            )
        )
