from schemas.base import APIModel


class DictionaryEntryOut(APIModel):
    term: str
    translation: str | None = None
    suggestions: list[str] = []
    definition: str | None = None
    phonetic: str | None = None
