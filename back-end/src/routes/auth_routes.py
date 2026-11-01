from fastapi import APIRouter, Response, status

from core.config import get_auth_settings
from routes.dependencies import AuthServiceDep, CurrentUserDep
from schemas.auth import LoginRequest, RegisterRequest
from schemas.user import UserOut

auth_routes = APIRouter(prefix="/auth", tags=["Auth"])


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
async def me(current_user: CurrentUserDep) -> UserOut:
    return current_user
