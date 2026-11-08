from schemas.base import APIModel


class ReadingThemeOut(APIModel):
    key: str
    label: str
    description: str


class ReadingSituationOut(APIModel):
    key: str
    title: str
    description: str


class ReadingTextOut(APIModel):
    theme: str
    situation: str
    title: str
    body: str
