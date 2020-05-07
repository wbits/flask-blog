from flaskblog.application.user_service import UserService
from flaskblog.application.command import Register, Login
from flaskblog.domain.error import UserNotFound, AuthenticationFailed
from flaskblog.infrastructure.controller.controller_service import ControllerServiceInterface
from flaskblog.infrastructure.form.registration_form import RegistrationForm
from flaskblog.infrastructure.form.login_form import LoginForm


class UserController:
    def __init__(self, controller_service: ControllerServiceInterface, user_service: UserService,
                 registration_form: RegistrationForm, login_form: LoginForm):
        self.__controller_service = controller_service
        self.__user_service = user_service
        self.__registration_form = registration_form
        self.__login_form = login_form

    def register(self):
        c = self.__controller_service
        f = self.__registration_form

        if c.session().is_authenticated():
            return c.redirect(c.url_for('home'))

        if f.validate_on_submit():
            register = Register(f.username.data, f.email.data, f.password.data)
            self.__user_service.create_account(register)

            c.flash('Your account has been created, you can login now!', 'success')

            return c.redirect(
                c.url_for('login')
            )

        return c.render_template('register.html', title='Register', form=f)

    def login(self):
        c = self.__controller_service
        f = self.__login_form

        if c.session().is_authenticated():
            return c.redirect(c.url_for('home'))

        if f.validate_on_submit():
            try:
                login = Login(f.email.data, f.password.data)
                user = self.__user_service.login(login)
                c.session().login(user, remember=f.remember.data)
                c.flash('You successfully logged in', 'success')
                return c.redirect(c.get_query_param('next', c.url_for('home')))
            except (UserNotFound, AuthenticationFailed):
                c.flash('Login failed, please check email and password', 'danger')

        return c.render_template('login.html', title='Login', form=f)
