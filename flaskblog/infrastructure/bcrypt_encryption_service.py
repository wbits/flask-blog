from flaskblog import bcrypt
from flaskblog.domain.encryption_service import EncryptionService
from flaskblog.domain.user import EncryptedPassword, Password


class BCryptEncryptionService(EncryptionService):
    @staticmethod
    def encrypt(password: Password) -> EncryptedPassword:
        hashed_password = bcrypt.generate_password_hash(str(password)).decode('utf-8')

        return EncryptedPassword(hashed_password)

    @staticmethod
    def validate(encrypted_password: EncryptedPassword, password: Password) -> bool:
        return bcrypt.check_password_hash(str(encrypted_password), str(password))
