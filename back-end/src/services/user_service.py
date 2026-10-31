from repositories.user_repository import UserRepository
from schemas.user import UserOut


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def list_users(self) -> list[UserOut]:
        return [
            UserOut(
                id=user.id,
                name=user.name,
                last_name=user.last_name,
                email=user.email,
                role=user.role,
            )
            for user in self._repository.list_all()
        ]
