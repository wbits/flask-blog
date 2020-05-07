from flaskblog.domain.user import User
from flaskblog.domain.value_objects import UserId, Email
import abc


class UserRepository(abc.ABC):
    @abc.abstractmethod
    def next_id(self) -> UserId:
        pass

    @abc.abstractmethod
    def save(self, user: User) -> None:
        pass

    @abc.abstractmethod
    def get(self, id: UserId) -> User:
        pass

    @abc.abstractmethod
    def get_by_email(self, email: Email) -> User:
        pass
