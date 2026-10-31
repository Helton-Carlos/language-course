from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response, status

from core.config import get_auth_settings
from core.database import SessionDep
from repositories.user_repository import UserRepository
from schemas.auth import LoginRequest, RegisterRequest
from schemas.user import UserOut
from services.auth_service import AuthService
from services.user_service import UserService

auth_routes = APIRouter(prefix="/auth", tags=["Auth"])


def get_auth_service(session: SessionDep) -> AuthService:
    repository = UserRepository(session)
    return AuthService(UserService(repository), repository)


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]


@auth_routes.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(data: RegisterRequest, service: AuthServiceDep) -> UserOut:
    return await service.register(data)


@auth_routes.post("/login", response_model=UserOut)
async def login(data: LoginRequest, response: Response, service: AuthServiceDep) -> UserOut:
    user, token = await service.login(data)
    settings = get_auth_settings()
    response.set_cookie(
        key=settings.cookie_name,
        value=token,
        max_age=settings.access_token_minutes * 60,
        httponly=True,
        secure=settings.cookie_secure,
        samesite="lax",
        path="/",
    )
    return user


@auth_routes.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(response: Response) -> None:
    settings = get_auth_settings()
    response.delete_cookie(
        key=settings.cookie_name,
        httponly=True,
        secure=settings.cookie_secure,
        samesite="lax",
        path="/",
    )


@auth_routes.get("/me", response_model=UserOut)
async def me(request: Request, service: AuthServiceDep) -> UserOut:
    token = request.cookies.get(get_auth_settings().cookie_name)
    return await service.get_current_user(token)
