#coding=utf-8

from flask_login import LoginManager
from flask_login import UserMixin
from .model import UserModel


class User(UserModel, UserMixin):
    def get_id(self):
        return self.id_


login_manager = LoginManager()
login_manager.login_view = 'web.index'
