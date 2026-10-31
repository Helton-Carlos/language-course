from typing import Annotated

from fastapi import APIRouter, Depends

from repositories.user_repository import UserRepository
from schemas.user import UserOut
from services.user_service import UserService

users_routes = APIRouter(tags=["Users"])


def get_user_service() -> UserService:
    return UserService(UserRepository())


UserServiceDep = Annotated[UserService, Depends(get_user_service)]


@users_routes.get("/users", response_model=list[UserOut])
async def get_users(service: UserServiceDep) -> list[UserOut]:
    return service.list_users()
