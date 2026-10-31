from core.exceptions import InvalidCredentialsError, UnauthorizedError
from core.security import (
    DUMMY_HASH,
    create_access_token,
    decode_access_token,
    verify_password,
)
from repositories.user_repository import UserRepository
from schemas.auth import LoginRequest, RegisterRequest
from schemas.user import UserCreate, UserOut
from services.user_service import UserService


class AuthService:
    def __init__(self, user_service: UserService, user_repository: UserRepository) -> None:
        self._user_service = user_service
        self._user_repository = user_repository

    async def register(self, data: RegisterRequest) -> UserOut:
        new_user = UserCreate(
            name=data.name,
            last_name=data.last_name,
            email=data.email,
            password=data.password,
        )
        return await self._user_service.create_user(new_user, role="user")

    async def login(self, data: LoginRequest) -> tuple[UserOut, str]:
        user = await self._user_repository.get_by_email(data.email)
        hashed = user.password_hash if user is not None else DUMMY_HASH
        password_ok = await verify_password(data.password, hashed)

        if user is None or not password_ok:
            raise InvalidCredentialsError()

        return UserOut.model_validate(user), create_access_token(user.id)

    async def get_current_user(self, token: str | None) -> UserOut:
        if not token:
            raise UnauthorizedError()

        user_id = decode_access_token(token)
        if user_id is None:
            raise UnauthorizedError()

        user = await self._user_repository.get(user_id)
        if user is None:
            raise UnauthorizedError()

        return UserOut.model_validate(user)
