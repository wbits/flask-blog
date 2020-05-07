from flaskblog.domain.user import User
from flaskblog.domain.user_repository import UserRepository
from flaskblog.domain.encryption_service import EncryptionService
from flaskblog.application.command import Register, Login
from flaskblog.domain.error import UserNotFound, AuthenticationFailed


class UserService:
    def __init__(self, repository: UserRepository, encryption_service: EncryptionService):
        self.__repository = repository
        self.__encryption_service = encryption_service

    def create_account(self, command: Register) -> User:
        user = User.register(
            self.__repository.next_id(),
            command.username(),
            command.email(),
            command.password(),
            self.__encryption_service,
        )

        self.__repository.save(user)

        return user

    def update_account(self):
        pass

    def login(self, command: Login) -> User:
        user = self.__repository.get_by_email(command.email())

        return user.authenticate(command.password(), self.__encryption_service)
