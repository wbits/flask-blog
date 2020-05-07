from flaskblog.infrastructure.form.registration_form import RegistrationForm
from flaskblog.infrastructure.form.login_form import LoginForm


def registration_form():
    return RegistrationForm()


def login_form():
    return LoginForm()
