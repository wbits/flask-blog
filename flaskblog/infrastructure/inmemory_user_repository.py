from flaskblog.domain.user_repository import UserRepository
from flaskblog.domain.value_objects import User
from flaskblog.domain.value_objects.user_id import UserId
from flaskblog.domain.value_objects.email import Email
from flaskblog.domain.error import UserNotFound


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.__users = {}
        self.__current_id = 0

    def next_id(self) -> UserId:
        return UserId(str(self.__current_id + 1))

    def save(self, user: User) -> None:
        self.__users.update({int(user.id()): user})

    def get(self, id: UserId) -> User:
        return self.__users.get(int(id))

    def get_by_email(self, email: Email) -> User:
        for user in self.__users.values():
            if user.email() == email:
                return user
        raise UserNotFound
