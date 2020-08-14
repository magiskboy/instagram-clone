#coding=utf-8

from ..repository import user as user_repo
from ..helper import exclude_unknown_args
from ..helper import catch_error


@catch_error()
@exclude_unknown_args
def get_user(username, password=None, verify=False):
    user = user_repo.get_user_by_username_or_email(username)
    if verify:
        if user and user.verify_password(password):
            return user
        raise ValueError('Sai tài khoản')
    return user


@catch_error()
def register_user(data):
    existed_user_fn = user_repo.check_user_existed
    if existed_user_fn(data['username']) or existed_user_fn(data['email']):
        raise ValueError('username hoặc email đã được sử dụng')
    return user_repo.create_user(data)
