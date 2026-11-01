from uuid import UUID

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
        if await self._language_repository.get(data.language_id) is None:
            raise LanguageNotFoundError()

        user = await self._user_repository.get(user_id)
        if user is None:
            raise UserNotFoundError()

        user = await self._user_repository.update(
            user,
            {"language_id": data.language_id, "level": data.level},
        )
        return UserOut.model_validate(user)
