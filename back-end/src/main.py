from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import get_settings
from core.database import check_connection, dispose_engine
from core.exceptions import register_exception_handlers
from routes.auth_routes import auth_routes
from routes.languages_routes import languages_routes
from routes.users_routes import users_routes

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    await check_connection()
    yield
    await dispose_engine()


app = FastAPI(title=settings.app_title, lifespan=lifespan)

register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)

app.include_router(auth_routes, prefix=settings.api_prefix)
app.include_router(languages_routes, prefix=settings.api_prefix)
app.include_router(users_routes, prefix=settings.api_prefix)
