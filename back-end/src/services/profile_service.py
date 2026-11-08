from uuid import UUID

from core.english import ENGLISH_ID
from core.exceptions import UserNotFoundError
from repositories.user_repository import UserRepository
from schemas.user import ProfileUpdate, UserOut


class ProfileService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def update_profile(self, user_id: UUID, data: ProfileUpdate) -> UserOut:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise UserNotFoundError()

        user = await self._user_repository.update(
            user,
            {"language_id": ENGLISH_ID, "level": data.level},
        )
        return UserOut.model_validate(user)
