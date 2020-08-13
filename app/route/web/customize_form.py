#coding=utf-8

from flask_wtf import FlaskForm
from wtforms.fields import StringField as StringFieldOriginal
from wtforms.fields import Field
from wtforms.fields import PasswordField as PasswordFieldOriginal
from wtforms.fields import SubmitField as SubmitFieldOriginal
from wtforms.fields import BooleanField as BooleanFieldOriginal
from wtforms.widgets.html5 import EmailInput
from wtforms.validators import Required
from wtforms.validators import Regexp
from wtforms.validators import EqualTo


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


class BooleanField(BooleanFieldOriginal, BootstrapField):
    pass
