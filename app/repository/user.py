#coding=utf-8

from sqlalchemy import or_
from ..model import db
from ..model import UserModel


def get_user_by_username_or_email(username_or_email):
    return UserModel.query.filter(or_(
        UserModel.email == username_or_email,
        UserModel.username == username_or_email
    )).first()
