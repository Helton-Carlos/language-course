from fastapi import APIRouter, Request, Response, status

from routes.cookies import clear_auth_cookie, read_auth_token, set_auth_cookie
from routes.dependencies import AuthServiceDep, CurrentUserDep
from schemas.auth import AccountDeleteRequest, LoginRequest, RegisterRequest
from schemas.user import UserOut

auth_routes = APIRouter(prefix="/auth", tags=["Auth"])


@auth_routes.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(data: RegisterRequest, service: AuthServiceDep) -> UserOut:
    return await service.register(data)


@auth_routes.post("/login", response_model=UserOut)
async def login(data: LoginRequest, response: Response, service: AuthServiceDep) -> UserOut:
    user, token = await service.login(data)
    set_auth_cookie(response, token)
    return user


@auth_routes.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(response: Response) -> None:
    clear_auth_cookie(response)


@auth_routes.delete("/account", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account(
    data: AccountDeleteRequest,
    current_user: CurrentUserDep,
    response: Response,
    service: AuthServiceDep,
) -> None:
    await service.delete_account(current_user.id, data.password)
    clear_auth_cookie(response)


@auth_routes.get("/me", response_model=UserOut | None)
async def me(request: Request, service: AuthServiceDep) -> UserOut | None:
    return await service.find_current_user(read_auth_token(request))
