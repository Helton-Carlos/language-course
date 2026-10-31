from typing import Literal

from schemas.base import APIModel

Role = Literal["admin", "user"]


class UserOut(APIModel):

    id: str
    name: str
    last_name: str | None = None
    email: str
    role: Role


class UserInDB(UserOut):

    password: str
