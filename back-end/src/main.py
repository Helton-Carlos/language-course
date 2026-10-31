from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import get_settings
from routes.languages_routes import languages_routes
from routes.users_routes import users_routes

settings = get_settings()

app = FastAPI(title=settings.app_title)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)

app.include_router(languages_routes, prefix=settings.api_prefix)
app.include_router(users_routes, prefix=settings.api_prefix)
