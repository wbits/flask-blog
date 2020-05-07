from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.infrastructure.model.user import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username: StringField) -> None:
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'A user with username {username.data} already exists')

    def validate_email(self, email: StringField) -> None:
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError(f'Given email address: {email.data} is already in use')
