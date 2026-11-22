from typing import Annotated

from fastapi import Depends, Request

from core.database import SessionDep
from repositories.activity_repository import ActivityRepository
from repositories.content_repository import ContentRepository
from repositories.lesson_repository import LessonRepository
from repositories.placement_repository import PlacementRepository
from repositories.reading_repository import ReadingRepository
from repositories.user_repository import UserRepository
from repositories.vocabulary_repository import VocabularyRepository
from routes.cookies import read_auth_token
from schemas.user import UserOut
from services.auth_service import AuthService
from services.content_service import ContentService
from services.dictionary_service import DictionaryService
from services.lesson_service import LessonService
from services.placement_service import PlacementService
from services.profile_service import ProfileService
from services.reading_service import ReadingService
from services.stats_service import StatsService
from services.user_service import UserService
from services.vocabulary_service import VocabularyService


def get_auth_service(session: SessionDep) -> AuthService:
    repository = UserRepository(session)
    return AuthService(UserService(repository), repository)


def get_user_service(session: SessionDep) -> UserService:
    return UserService(UserRepository(session))


def get_profile_service(session: SessionDep) -> ProfileService:
    return ProfileService(UserRepository(session))


def get_placement_service(session: SessionDep) -> PlacementService:
    return PlacementService(PlacementRepository(session))


def get_content_service(session: SessionDep) -> ContentService:
    return ContentService(ContentRepository(session))


def get_reading_service(session: SessionDep) -> ReadingService:
    return ReadingService(ReadingRepository(session))


def get_vocabulary_service(session: SessionDep) -> VocabularyService:
    return VocabularyService(VocabularyRepository(session), ActivityRepository(session))


def get_lesson_service(session: SessionDep) -> LessonService:
    return LessonService(LessonRepository(session))


def get_stats_service(session: SessionDep) -> StatsService:
    return StatsService(VocabularyRepository(session), ActivityRepository(session))


def get_dictionary_service() -> DictionaryService:
    return DictionaryService()


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
UserServiceDep = Annotated[UserService, Depends(get_user_service)]
ProfileServiceDep = Annotated[ProfileService, Depends(get_profile_service)]
PlacementServiceDep = Annotated[PlacementService, Depends(get_placement_service)]
ContentServiceDep = Annotated[ContentService, Depends(get_content_service)]
ReadingServiceDep = Annotated[ReadingService, Depends(get_reading_service)]
VocabularyServiceDep = Annotated[VocabularyService, Depends(get_vocabulary_service)]
LessonServiceDep = Annotated[LessonService, Depends(get_lesson_service)]
StatsServiceDep = Annotated[StatsService, Depends(get_stats_service)]
DictionaryServiceDep = Annotated[DictionaryService, Depends(get_dictionary_service)]


async def get_current_user(request: Request, service: AuthServiceDep) -> UserOut:
    return await service.get_current_user(read_auth_token(request))


CurrentUserDep = Annotated[UserOut, Depends(get_current_user)]
