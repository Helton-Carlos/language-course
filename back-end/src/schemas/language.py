from uuid import UUID

from schemas.base import APIModel


class LanguageOut(APIModel):
    id: UUID
    code: str
    name: str
    name_pt: str
    prefix: str
    description: str
    countries: list[str]
