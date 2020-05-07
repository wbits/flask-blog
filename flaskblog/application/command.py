from flaskblog.domain.value_objects import Username, Email, Password


class Register:
    def __init__(self, username: str, email: str, password: str):
        self.__username = Username(username)
        self.__email = Email(email)
        self.__password = Password(password)

    def username(self) -> Username:
        return self.__username

    def email(self) -> Email:
        return self.__email

    def password(self) -> Password:
        return self.__password


class Login:
    def __init__(self, email: str, password: str):
        self.__email = Email(email)
        self.__password = Password(password)

    def email(self) -> Email:
        return self.__email

    def password(self) -> Password:
        return self.__password
