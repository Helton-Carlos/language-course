from uuid import UUID

from core.config import APP_LANGUAGE_CODE
from core.exceptions import LanguageNotFoundError, UserNotFoundError
from repositories.language_repository import LanguageRepository
from repositories.user_repository import UserRepository
from schemas.user import ProfileUpdate, UserOut


class ProfileService:
    def __init__(
        self,
        user_repository: UserRepository,
        language_repository: LanguageRepository,
    ) -> None:
        self._user_repository = user_repository
        self._language_repository = language_repository

    async def update_profile(self, user_id: UUID, data: ProfileUpdate) -> UserOut:
        language = await self._language_repository.get_by_code(APP_LANGUAGE_CODE)
        if language is None:
            raise LanguageNotFoundError()

        user = await self._user_repository.get(user_id)
        if user is None:
            raise UserNotFoundError()

        user = await self._user_repository.update(
            user,
            {"language_id": language.id, "level": data.level},
        )
        return UserOut.model_validate(user)
