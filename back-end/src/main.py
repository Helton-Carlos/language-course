from fastapi import FastAPI
from routes.languages_routes import languages_routes

app = FastAPI(title="Language Course API")

app.include_router(languages_routes)