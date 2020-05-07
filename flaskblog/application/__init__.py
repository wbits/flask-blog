from flaskblog.application.user_service import UserService
from flaskblog.infrastructure import user_repository
from flaskblog.infrastructure import encryption_service


def user_service():
    return UserService(user_repository(), encryption_service())
