from typing import Annotated, Literal
from uuid import UUID

from pydantic import AfterValidator, EmailStr, Field

from schemas.base import APIModel

Role = Literal["admin", "user"]

Name = Annotated[str, Field(min_length=1, max_length=100)]
Email = Annotated[EmailStr, AfterValidator(str.lower)]
Password = Annotated[str, Field(min_length=8, max_length=128)]


class UserCreate(APIModel):
    name: Name
    last_name: Name | None = None
    email: Email
    password: Password


class UserUpdate(APIModel):
    name: Name | None = None
    last_name: Name | None = None
    email: Email | None = None


class UserOut(APIModel):
    id: UUID
    name: str
    last_name: str | None = None
    email: str
    role: Role
