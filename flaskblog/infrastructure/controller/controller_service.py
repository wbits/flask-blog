import abc
from typing import Callable
from flaskblog.domain.session import Session


class ControllerServiceInterface(abc.ABC):
    @abc.abstractmethod
    def redirect(self, location: str):
        pass

    @abc.abstractmethod
    def url_for(self, route: str) -> str:
        pass

    @abc.abstractmethod
    def flash(self, message: str, category: str):
        pass

    @abc.abstractmethod
    def render_template(self, template_name: str, **context):
        pass

    @abc.abstractmethod
    def session(self) -> Session:
        pass

    @abc.abstractmethod
    def get_query_param(self, param, default=None):
        pass


class ControllerService(ControllerServiceInterface):
    def __init__(self, redirect: Callable, url_for: Callable, flash: Callable, render_template: Callable,
                 request, session: Session):
        self.__session = session
        self.__redirect = redirect
        self.__url_for = url_for
        self.__flash = flash
        self.__request = request
        self.__render_template = render_template

    def redirect(self, location: str):
        return self.__redirect(location)

    def url_for(self, route: str, **values) -> str:
        return self.__url_for(route, **values)

    def flash(self, message: str, category: str) -> None:
        self.__flash(message, category)

    def render_template(self, template_name, **context):
        return self.__render_template(template_name, **context)

    def get_query_param(self, param, default=None):
        return self.__request.args.get(param, default)

    def session(self) -> Session:
        return self.__session
