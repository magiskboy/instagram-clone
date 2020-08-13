#coding=utf-8

from flask_wtf import FlaskForm
from wtforms.widgets.html5 import EmailInput
from wtforms.validators import Required
from wtforms.validators import Regexp
from wtforms.validators import EqualTo
from .customize_form import StringField
from .customize_form import PasswordField
from .customize_form import BooleanField
from .customize_form import SubmitField


USERNAME_REGEX = r'^[a-zA-Z0-9_]{6,20}$'
PASSWORD_REGEX = r'^[a-zA-Z0-9_]{6,20}$'


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Regexp(USERNAME_REGEX)])
    password = PasswordField('Password', validators=[Required(), Regexp(PASSWORD_REGEX)])
    remember = BooleanField('Remember me?', default=False)
    submit = SubmitField('Login')


class RegisterForm(LoginForm):
    fullname = StringField('Fullname', validators=[Required()])
    email = StringField('Email', validators=[Required()], widget=EmailInput())
    confirm = PasswordField(validators=[EqualTo('password')])
    submit = SubmitField('Register')
