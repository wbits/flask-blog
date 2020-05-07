from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.infrastructure.model.user import User
from flask_login import current_user


# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign up')
#
#     def validate_username(self, username: StringField) -> None:
#         value_objects = User.query.filter_by(username=username.data).first()
#         if value_objects:
#             raise ValidationError(f'A value_objects with username {username.data} already exists')
#
#     def validate_email(self, email: StringField) -> None:
#         value_objects = User.query.filter_by(username=email.data).first()
#         if value_objects:
#             raise ValidationError(f'Given email address: {email.data} is already in use')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username: StringField) -> None:
        if current_user.username == username.data:
            return
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'A user with username {username.data} already exists')

    def validate_email(self, email: StringField) -> None:
        if current_user.email == email.data:
            return
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError(f'Given email address: {email.data} is already in use')


# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
