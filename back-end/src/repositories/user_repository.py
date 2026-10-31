from data.users import USERS
from schemas.user import UserInDB


class UserRepository:

    def list_all(self) -> list[UserInDB]:
        return [UserInDB.model_validate(item) for item in USERS]
