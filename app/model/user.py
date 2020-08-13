#coding=utf-8

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from . import db
from . import BaseModel
from . import QueryWithSoftDelete


class UserModel(BaseModel, UserMixin, db.Model):
    __tablename__ = 'users'
    query_class = QueryWithSoftDelete

    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    fullname = Column(String(100), nullable=False)
    is_active = Column(Boolean())
    deleted = db.Column(db.Boolean(), default=False)

    def get_id(self):
        return self.id_

    @property
    def password(self):
        return NotImplemented

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
