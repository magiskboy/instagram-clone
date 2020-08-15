#coding=utf-8

from flask_wtf import FlaskForm
from wtforms.widgets.html5 import EmailInput
from wtforms.validators import Length
from ._base import StringField
from ._base import FileField
from ._base import SubmitField
from ._base import BooleanField


class UpdatePersonalPageForm(FlaskForm):
    avatar = FileField('Avatar')
    fullname = StringField('Fullname')
    username = StringField('Username')
    email = StringField('Email', widget=EmailInput())
    phone_number = StringField('Phone number', validators=[Length(10, 11)])
    gender = BooleanField('Gender')
