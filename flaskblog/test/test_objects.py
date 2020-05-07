from flaskblog.domain.value_objects import User
from flaskblog.domain.value_objects.user_id import UserId
from flaskblog.domain.value_objects.username import Username
from flaskblog.domain.value_objects.email import Email
from flaskblog.domain.value_objects.password import Password
from flaskblog.domain.value_objects.encrypted_password import EncryptedPassword
from flaskblog.infrastructure.bcrypt_encryption_service import BCryptEncryptionService


def encrypt(password: Password) -> EncryptedPassword:
    encryption = BCryptEncryptionService()
    return encryption.encrypt(password)


def user(**values):
    if values.get('encrypted_password', False):
        password = EncryptedPassword(values['encrypted_password'])
    else:
        password = encrypt(Password(values['password']))

    return User(UserId(values['id']), Username(values['username']), Email(values['email']),
                password)
