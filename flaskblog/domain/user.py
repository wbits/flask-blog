from flaskblog.domain.encryption_service import EncryptionService, Password, EncryptedPassword
from flaskblog.domain.error import AuthenticationFailed
from flaskblog.domain.value_objects import UserId, Username, Email, ProfilePicture


class User:
    def __init__(self, id: UserId, username: Username, email: Email, password: EncryptedPassword):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__password = password

    @staticmethod
    def register(id: UserId, username: Username, email: Email, password: Password,
                 encryption_service: EncryptionService):
        encrypted_password = encryption_service.encrypt(password)

        return User(id, username, email, encrypted_password)

    def authenticate(self, password: Password, encryption_service: EncryptionService):
        if encryption_service.validate(self.__password, password):
            return self
        else:
            raise AuthenticationFailed

    def id(self) -> UserId:
        return self.__id

    def username(self) -> Username:
        return self.__username

    def email(self) -> Email:
        return self.__email

    def password(self) -> EncryptedPassword:
        return self.__password

    def profile_picture(self) -> ProfilePicture:
        return ProfilePicture('default.jpg')
