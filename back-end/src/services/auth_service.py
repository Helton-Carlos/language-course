from schemas.auth import RegisterRequest
from schemas.user import UserCreate, UserOut
from services.user_service import UserService


class AuthService:
    def __init__(self, user_service: UserService) -> None:
        self._user_service = user_service

    async def register(self, data: RegisterRequest) -> UserOut:
        new_user = UserCreate(
            name=data.name,
            last_name=data.last_name,
            email=data.email,
            password=data.password,
        )
        return await self._user_service.create_user(new_user, role="user")
