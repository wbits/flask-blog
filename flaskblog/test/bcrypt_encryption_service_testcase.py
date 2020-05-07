import unittest
from flaskblog.infrastructure.bcrypt_encryption_service import BCryptEncryptionService
from flaskblog.domain.value_objects.encrypted_password import EncryptedPassword
from flaskblog.domain.value_objects.password import Password


class BCryptEncryptionServiceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.__encryption_service = BCryptEncryptionService()

    def test_it_encrypts_and_validates(self):
        password = Password('test')
        encrypted_password = self.__encryption_service.encrypt(password)

        self.assertIsInstance(encrypted_password, EncryptedPassword)
        self.assertTrue(self.__encryption_service.validate(encrypted_password, password))
        self.assertFalse(self.__encryption_service.validate(encrypted_password, Password('something')))


if __name__ == '__main__':
    unittest.main()
