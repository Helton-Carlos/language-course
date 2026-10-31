from fastapi import APIRouter

from utils.users import USERS

users_routes = APIRouter(tags=['Users'])

@users_routes.get("/users")
async def get_users_routes() -> list[dict[str, str | list[str]]]:
    return USERS