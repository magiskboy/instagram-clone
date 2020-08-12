#coding=utf-8

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from . import db
from . import BaseModel


class UserModel(db.Model, BaseModel):
    __tablename__ = 'users'

    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    is_active = Column(Boolean())

    @property
    def password(self):
        return NotImplemented

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def password_verify(self, password):
        return check_password_hash(self.password_hash, password)
