class UserId:
    def __init__(self, id: str):
        self.__id = id

    def __int__(self) -> int:
        return int(self.__id)


class Username:
    def __init__(self, username: str):
        self.__username = username

    def __str__(self) -> str:
        return self.__username


class Email:
    def __init__(self, email: str):
        self.__email = email

    def __str__(self) -> str:
        return self.__email

    def __eq__(self, other) -> bool:
        if not isinstance(other, Email):
            return False

        return self.__email == other.__email


class EncryptedPassword:
    def __init__(self, password: str):
        self.__password = password

    def __str__(self) -> str:
        return self.__password


class Password:
    def __init__(self, password: str):
        self.__password = password

    def __str__(self) -> str:
        return self.__password


class ProfilePicture:
    def __init__(self, filename: str):
        self.__filename = filename

    def __str__(self) -> str:
        return self.__filename
