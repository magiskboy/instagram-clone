#coding=utf-8

from flask_wtf import FlaskForm
from wtforms.fields import StringField as StringFieldOriginal
from wtforms.fields import Field
from wtforms.fields import PasswordField as PasswordFieldOriginal
from wtforms.fields import SubmitField as SubmitFieldOriginal
from wtforms.widgets.html5 import EmailInput
from wtforms.validators import Required
from wtforms.validators import Regexp
from wtforms.validators import EqualTo


USERNAME_REGEX = r'^[a-zA-Z0-9_]{6,20}$'
PASSWORD_REGEX = r'^[a-zA-Z0-9_]{6,20}$'


class BootstrapField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.render_kw = {
            'class': 'form-control'
        }


class StringField(StringFieldOriginal, BootstrapField):
    pass


class PasswordField(PasswordFieldOriginal, BootstrapField):
    pass


class SubmitField(SubmitFieldOriginal, BootstrapField):
    pass


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Regexp(USERNAME_REGEX)])
    password = PasswordField('Password', validators=[Required(), Regexp(PASSWORD_REGEX)])
    submit = SubmitField('Login')


class RegisterForm(LoginForm):
    email = StringField('Email', validators=[Required()], widget=EmailInput())
    confirm = PasswordField(validators=[EqualTo('password')])
    submit = SubmitField('Register')
