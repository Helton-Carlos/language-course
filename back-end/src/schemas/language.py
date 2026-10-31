from typing import Annotated
from uuid import UUID

from pydantic import Field

from schemas.base import APIModel

Code = Annotated[str, Field(pattern=r"^[a-z]{2,3}-[A-Z]{2}$", max_length=10)]
Prefix = Annotated[str, Field(pattern=r"^[A-Z]{2}$")]
Name = Annotated[str, Field(min_length=1, max_length=100)]
Description = Annotated[str, Field(min_length=1)]
Countries = list[Annotated[str, Field(min_length=1, max_length=100)]]


class LanguageCreate(APIModel):
    code: Code
    name: Name
    name_pt: Name
    prefix: Prefix
    description: Description
    countries: Countries = Field(default_factory=list)


class LanguageUpdate(APIModel):
    code: Code | None = None
    name: Name | None = None
    name_pt: Name | None = None
    prefix: Prefix | None = None
    description: Description | None = None
    countries: Countries | None = None


class LanguageOut(LanguageCreate):
    id: UUID
