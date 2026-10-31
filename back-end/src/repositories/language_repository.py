from data.languages import LANGUAGES
from schemas.language import LanguageOut


class LanguageRepository:

    def list_all(self) -> list[LanguageOut]:
        return [LanguageOut.model_validate(item) for item in LANGUAGES]
