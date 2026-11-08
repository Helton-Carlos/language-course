from core.exceptions import ReadingTextNotFoundError
from core.reading import READING_SITUATIONS, READING_THEMES, band_for_level
from repositories.reading_repository import ReadingRepository
from schemas.reading import ReadingSituationOut, ReadingTextOut, ReadingThemeOut


class ReadingService:
    def __init__(self, repository: ReadingRepository) -> None:
        self._repository = repository

    def list_themes(self) -> list[ReadingThemeOut]:
        return [ReadingThemeOut(**theme) for theme in READING_THEMES]

    def list_situations(self, theme: str) -> list[ReadingSituationOut]:
        situations = READING_SITUATIONS.get(theme)
        if situations is None:
            raise ReadingTextNotFoundError()
        return [ReadingSituationOut(**situation) for situation in situations]

    async def get_text(self, theme: str, situation: str, level: str | None) -> ReadingTextOut:
        keys = {item["key"] for item in READING_SITUATIONS.get(theme, [])}
        if situation not in keys:
            raise ReadingTextNotFoundError()

        text = await self._repository.get(theme, situation, band_for_level(level))
        if text is None:
            raise ReadingTextNotFoundError()

        return ReadingTextOut(theme=theme, situation=situation, title=text.title, body=text.body)
