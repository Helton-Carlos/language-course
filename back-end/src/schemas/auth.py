from typing import Self

from pydantic import model_validator

from schemas.user import UserCreate


class RegisterRequest(UserCreate):
    password_confirm: str

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        if self.password != self.password_confirm:
            raise ValueError("As senhas não conferem")
        return self
