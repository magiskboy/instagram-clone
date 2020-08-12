#coding=utf-8

from ..repository import user as user_repo


def get_and_verify_user(username_or_email, password):
    user = user_repo.get_user_by_username_or_email(username_or_email)
    if user and user.verify_password(password):
        return user
    return None
