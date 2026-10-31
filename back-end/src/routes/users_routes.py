from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Response, status

from core.database import SessionDep
from repositories.user_repository import UserRepository
from schemas.user import UserCreate, UserOut, UserUpdate
from services.user_service import UserService

users_routes = APIRouter(tags=["Users"])


def get_user_service(session: SessionDep) -> UserService:
    return UserService(UserRepository(session))


UserServiceDep = Annotated[UserService, Depends(get_user_service)]


@users_routes.get("/users", response_model=list[UserOut])
async def list_users(service: UserServiceDep) -> list[UserOut]:
    return await service.list_users()


@users_routes.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: UUID, service: UserServiceDep) -> UserOut:
    return await service.get_user(user_id)


@users_routes.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(data: UserCreate, service: UserServiceDep) -> UserOut:
    return await service.create_user(data)


@users_routes.patch("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: UUID, data: UserUpdate, service: UserServiceDep) -> UserOut:
    return await service.update_user(user_id, data)


@users_routes.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: UUID, service: UserServiceDep) -> Response:
    await service.delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
