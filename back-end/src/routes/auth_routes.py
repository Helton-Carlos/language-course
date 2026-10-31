from typing import Annotated

from fastapi import APIRouter, Depends, status

from core.database import SessionDep
from repositories.user_repository import UserRepository
from schemas.auth import RegisterRequest
from schemas.user import UserOut
from services.auth_service import AuthService
from services.user_service import UserService

auth_routes = APIRouter(prefix="/auth", tags=["Auth"])


def get_auth_service(session: SessionDep) -> AuthService:
    return AuthService(UserService(UserRepository(session)))


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]


@auth_routes.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(data: RegisterRequest, service: AuthServiceDep) -> UserOut:
    return await service.register(data)
