from repositories.language_repository import LanguageRepository
from schemas.language import LanguageOut


class LanguageService:
    def __init__(self, repository: LanguageRepository) -> None:
        self._repository = repository

    def list_languages(self) -> list[LanguageOut]:
        return self._repository.list_all()
