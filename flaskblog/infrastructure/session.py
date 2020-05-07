from flaskblog.domain.session import Session as SessionInterface
from flaskblog.domain.value_objects import UserId, Username
from flaskblog.domain.user import User
from flaskblog.infrastructure.model.user import User as OrmUser
from typing import Callable


class Session(SessionInterface):
    def __init__(self, current_user, login_user: Callable, logout_user: Callable):
        self.__current_user = current_user
        self.__login_user = login_user
        self.__logout_user = logout_user

    def is_authenticated(self) -> bool:
        return self.__current_user.is_authenticated

    def login(self, user: User, remember: bool) -> bool:
        return self.__login_user(OrmUser.from_domain_user(user), remember)

    def logout(self) -> bool:
        return self.__logout_user()

    def current_user_id(self) -> UserId:
        return UserId(str(self.__current_user.id))

    def current_user_name(self) -> Username:
        return Username(self.__current_user.username)
