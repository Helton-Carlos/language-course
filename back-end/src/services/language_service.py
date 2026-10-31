from uuid import UUID

from core.exceptions import LanguageCodeAlreadyExistsError, LanguageNotFoundError
from models.language import Language
from repositories.language_repository import LanguageRepository
from schemas.language import LanguageCreate, LanguageOut, LanguageUpdate


class LanguageService:
    def __init__(self, repository: LanguageRepository) -> None:
        self._repository = repository

    async def list_languages(self) -> list[LanguageOut]:
        languages = await self._repository.list_all()
        return [LanguageOut.model_validate(language) for language in languages]

    async def get_language(self, language_id: UUID) -> LanguageOut:
        language = await self._get_or_raise(language_id)
        return LanguageOut.model_validate(language)

    async def create_language(self, data: LanguageCreate) -> LanguageOut:
        await self._ensure_code_available(data.code)
        language = await self._repository.add(data.model_dump())
        return LanguageOut.model_validate(language)

    async def update_language(self, language_id: UUID, data: LanguageUpdate) -> LanguageOut:
        language = await self._get_or_raise(language_id)
        values = data.model_dump(exclude_none=True)

        new_code = values.get("code")
        if new_code is not None and new_code != language.code:
            await self._ensure_code_available(new_code)

        language = await self._repository.update(language, values)
        return LanguageOut.model_validate(language)

    async def delete_language(self, language_id: UUID) -> None:
        language = await self._get_or_raise(language_id)
        await self._repository.delete(language)

    async def _get_or_raise(self, language_id: UUID) -> Language:
        language = await self._repository.get(language_id)
        if language is None:
            raise LanguageNotFoundError()
        return language

    async def _ensure_code_available(self, code: str) -> None:
        if await self._repository.get_by_code(code) is not None:
            raise LanguageCodeAlreadyExistsError()
