from typing import Annotated

from fastapi import APIRouter, Query

from routes.dependencies import CurrentUserDep, DictionaryServiceDep
from schemas.dictionary import DictionaryEntryOut
from schemas.vocabulary import Term

dictionary_routes = APIRouter(prefix="/dictionary", tags=["Dictionary"])


@dictionary_routes.get("/lookup", response_model=DictionaryEntryOut)
async def lookup(
    term: Annotated[Term, Query(max_length=200)],
    _: CurrentUserDep,
    service: DictionaryServiceDep,
) -> DictionaryEntryOut:
    return await service.lookup(term)
