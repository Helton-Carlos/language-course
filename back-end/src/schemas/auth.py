from typing import Annotated, Self

from pydantic import Field, model_validator

from schemas.base import APIModel
from schemas.user import Email, UserCreate


class RegisterRequest(UserCreate):
    password_confirm: str

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        if self.password != self.password_confirm:
            raise ValueError("As senhas não conferem")
        return self


class LoginRequest(APIModel):
    email: Email
    password: Annotated[str, Field(min_length=1, max_length=128)]


class AccountDeleteRequest(APIModel):
    password: Annotated[str, Field(min_length=1, max_length=128)]
