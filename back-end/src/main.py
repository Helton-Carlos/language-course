from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.languages_routes import languages_routes

app = FastAPI(title="Language Course API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://127.0.0.1:3001"],
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)

app.include_router(languages_routes, prefix="/api")
