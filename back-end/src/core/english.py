from uuid import UUID

from core.exceptions import LanguageNotFoundError

ENGLISH_ID = UUID("6f1c2d3e-4a5b-4c6d-8e7f-9a0b1c2d3e4f")

ENGLISH = {
    "id": ENGLISH_ID,
    "code": "en-US",
    "name": "English",
    "name_pt": "inglês",
    "prefix": "US",
    "description": "Idioma mais usado nos negócios, na ciência, no turismo e na internet. É a principal língua de comunicação entre pessoas de países diferentes.",
    "countries": ["Estados Unidos", "Reino Unido", "Canadá", "Austrália", "Nova Zelândia", "Irlanda"],
}


def ensure_english(language_id: UUID) -> None:
    if language_id != ENGLISH_ID:
        raise LanguageNotFoundError()
