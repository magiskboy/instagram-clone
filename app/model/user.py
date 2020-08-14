#coding=utf-8

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from . import db
from . import BaseModel
from . import QueryWithSoftDelete


class FriendRelationship(BaseModel, db.Model):
    __tablename__ = 'friend_relationships'

    left_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    right_id = Column(Integer(), ForeignKey('users.id'), nullable=False)


class FollowRelationship(BaseModel, db.Model):
    __tablename__ = 'follow_relationships'

    left_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    right_id = Column(Integer(), ForeignKey('users.id'), nullable=False)


class UserModel(BaseModel, UserMixin, db.Model):
    __tablename__ = 'users'
    query_class = QueryWithSoftDelete

    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    fullname = Column(String(100), nullable=False)
    is_active = Column(Boolean())
    phone_number = Column(String(11))
    photo_url = Column(String(255))
    gender = Column(Boolean())
    deleted = db.Column(db.Boolean(), default=False)

    friends = relationship('UserModel',
                           secondary=FriendRelationship,
                           primaryjoin='UserModel.id_ == FriendRelationship.left_id',
                           secondaryjoin='FriendRelationship.right_id == UserModel.id_')

    follwings = relationship('UserModel',
                             secondary=FollowRelationship,
                             primaryjoin='UserModel.id_ == FollowRelationship.left_id',
                             secondaryjoin='FollowRelationship.right_id == UserModel.id_')

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
