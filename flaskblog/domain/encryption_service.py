from flaskblog.domain.value_objects import Password, EncryptedPassword
import abc


class EncryptionService(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def encrypt(password: Password) -> EncryptedPassword:
        pass

    @staticmethod
    @abc.abstractmethod
    def validate(encrypted_password: EncryptedPassword, password: Password) -> bool:
        pass
