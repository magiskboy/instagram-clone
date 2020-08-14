#coding=utf-8

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from ._base import BaseModel
from ._base import db


class Post(BaseModel, db.Model):
    __tablename__ = 'posts'

    user_id = Column(Integer(), ForeignKey('users.id_'), nullable=False)

    photos = relationship('Photo')
    likes = relationship('Like')
    comments = relationship('Comment')


class Photo(BaseModel, db.Model):
    __tablename__ = 'photos'

    post_id = Column(Integer(), ForeignKey('posts.id_'), nullable=False)
    url = Column(String(255), nullable=False)


class Like(BaseModel, db.Model):
    __tablename__ = 'likes'

    post_id = Column(Integer(), ForeignKey('posts.id_'), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id_'), nullable=False)


class Comment(BaseModel, db.Model):
    __tablename__ = 'comments'

    post_id = Column(Integer(), ForeignKey('posts.id_'), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id_'), nullable=False)
    content = Column(String(200), nullable=False)
