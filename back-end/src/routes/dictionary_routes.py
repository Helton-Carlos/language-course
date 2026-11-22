from typing import Annotated

from fastapi import APIRouter, Depends, Query

from routes.dependencies import CurrentUserDep
from schemas.dictionary import DictionaryEntryOut
from schemas.vocabulary import Term
from services.dictionary_service import DictionaryService

dictionary_routes = APIRouter(prefix="/dictionary", tags=["Dictionary"])


def get_dictionary_service() -> DictionaryService:
    return DictionaryService()


DictionaryServiceDep = Annotated[DictionaryService, Depends(get_dictionary_service)]


@dictionary_routes.get("/lookup", response_model=DictionaryEntryOut)
async def lookup(
    term: Annotated[Term, Query(max_length=200)],
    _: CurrentUserDep,
    service: DictionaryServiceDep,
) -> DictionaryEntryOut:
    return await service.lookup(term)
