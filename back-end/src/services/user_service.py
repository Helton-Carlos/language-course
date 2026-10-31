from uuid import UUID

from core.exceptions import UserEmailAlreadyExistsError, UserNotFoundError
from core.security import hash_password
from models.user import User
from repositories.user_repository import UserRepository
from schemas.user import Role, UserCreate, UserOut, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    async def list_users(self) -> list[UserOut]:
        users = await self._repository.list_all()
        return [UserOut.model_validate(user) for user in users]

    async def get_user(self, user_id: UUID) -> UserOut:
        user = await self._get_or_raise(user_id)
        return UserOut.model_validate(user)

    async def create_user(self, data: UserCreate, role: Role = "user") -> UserOut:
        await self._ensure_email_available(data.email)
        values = data.model_dump(exclude={"password"})
        values["password_hash"] = await hash_password(data.password)
        values["role"] = role
        user = await self._repository.add(values)
        return UserOut.model_validate(user)

    async def update_user(self, user_id: UUID, data: UserUpdate) -> UserOut:
        user = await self._get_or_raise(user_id)
        values = data.model_dump(exclude_none=True)

        new_email = values.get("email")
        if new_email is not None and new_email != user.email:
            await self._ensure_email_available(new_email)

        user = await self._repository.update(user, values)
        return UserOut.model_validate(user)

    async def delete_user(self, user_id: UUID) -> None:
        user = await self._get_or_raise(user_id)
        await self._repository.delete(user)

    async def _get_or_raise(self, user_id: UUID) -> User:
        user = await self._repository.get(user_id)
        if user is None:
            raise UserNotFoundError()
        return user

    async def _ensure_email_available(self, email: str) -> None:
        if await self._repository.get_by_email(email) is not None:
            raise UserEmailAlreadyExistsError()
