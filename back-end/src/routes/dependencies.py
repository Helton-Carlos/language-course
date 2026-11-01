from typing import Annotated

from fastapi import Depends, Request

from core.config import get_auth_settings
from core.database import SessionDep
from repositories.user_repository import UserRepository
from schemas.user import UserOut
from services.auth_service import AuthService
from services.user_service import UserService


def get_auth_service(session: SessionDep) -> AuthService:
    repository = UserRepository(session)
    return AuthService(UserService(repository), repository)


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]


async def get_current_user(request: Request, service: AuthServiceDep) -> UserOut:
    token = request.cookies.get(get_auth_settings().cookie_name)
    return await service.get_current_user(token)


CurrentUserDep = Annotated[UserOut, Depends(get_current_user)]
