import unittest
from flaskblog.application.command import Register, Login
from flaskblog.application.user_service import UserService
from flaskblog.domain.encryption_service import EncryptionService
from flaskblog.domain.value_objects.encrypted_password import EncryptedPassword
from flaskblog.domain.value_objects.password import Password
from flaskblog.domain.error import UserNotFound, AuthenticationFailed
from flaskblog.infrastructure.inmemory_user_repository import InMemoryUserRepository
import flaskblog.test.test_objects as test_objects


class FakeEncryptionService(EncryptionService):
    @staticmethod
    def encrypt(password: Password) -> EncryptedPassword:
        return EncryptedPassword(str(password))

    @staticmethod
    def validate(encrypted_password: EncryptedPassword, password: Password) -> bool:
        return str(encrypted_password) == str(password)


class UserServiceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.__repository = InMemoryUserRepository()
        self.__user_service = UserService(self.__repository, FakeEncryptionService())

    def test_it_can_create_an_account(self):
        command = Register('some username', 'foo@bar.zoo', 'p455w0r6')
        user = self.__user_service.create_account(command)

        self.assertEqual(user, self.__repository.get(user.id()))

    def test_it_can_login_a_user(self):
        email = 'foo@bar.baz'
        password = 'p455w)r6'
        user = test_objects.user(
            id='1',
            username='some username',
            email=email,
            encrypted_password=password
        )
        self.__repository.save(user)

        self.assertEqual(user, self.__user_service.login(Login(email, password)))
        self.assertRaises(UserNotFound, self.__user_service.login, Login('something@not.valid', password))
        self.assertRaises(AuthenticationFailed, self.__user_service.login, Login(email, 'wrong_password'))


if __name__ == '__main__':
    unittest.main()
