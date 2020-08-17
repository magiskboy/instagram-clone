#coding=utf-8

from functools import lru_cache
from sqlalchemy import or_
from sqlalchemy import func
from sqlalchemy import exists
from sqlalchemy.orm import aliased
from ..model import db
from ..model import UserModel
from ..model import FriendRelationship
from ..model import FollowRelationship


@lru_cache
def get_user_by_username_or_email(username_or_email):
    return UserModel.query.filter(or_(
        UserModel.email == username_or_email,
        UserModel.username == username_or_email
    )).first()


def create_user(data):
    new_user = UserModel(**data)
    new_user.password = data['password']
    new_user.save()
    return new_user


def check_user_existed(username_or_email):
    return db.session.query(exists().where(or_(
        UserModel.username == username_or_email,
        UserModel.email == username_or_email,
    ))).scalar()


def get_personal_info(username):
    return get_user_by_username_or_email(username)
