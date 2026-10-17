from fastapi import FastAPI

from utils.languages import LANGUAGES

app = FastAPI(title="Language Course API")

@app.get("/languages")
def get_languages() -> list[dict[str, str]]:
    return LANGUAGES
