import abc
from flaskblog.domain.value_objects import UserId, Username
from flaskblog.domain.user import User


class Session(abc.ABC):
    @abc.abstractmethod
    def is_authenticated(self) -> bool:
        pass

    @abc.abstractmethod
    def login(self, user: User, remember: bool) -> bool:
        pass

    @abc.abstractmethod
    def logout(self) -> bool:
        pass

    @abc.abstractmethod
    def current_user_id(self) -> UserId:
        pass

    @abc.abstractmethod
    def current_user_name(self) -> Username:
        pass
