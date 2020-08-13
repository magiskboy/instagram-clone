#coding=utf-8

from inspect import getfullargspec
from flask import flash
from flask import redirect
from flask import url_for


def flash_and_redirect(name_module, messages=None):
    if messages:
        for message in messages:
            flash(message)
    return redirect(url_for(name_module))


def exclude_unknown_args(f):
    def decorator(*args, **kwargs):
        spec = getfullargspec(f)
        filterd_args = {k: v for k, v in kwargs.items() if k in spec.args}
        return f(*args, **filterd_args)
    return decorator


def catch_error(return_msg=True, exc_class=Exception):
    def decorator(f):
        def new_func(*args, **kwargs):
            try:
                ret = f(*args, **kwargs)
            except exc_class as err:
                if return_msg:
                    return str(err), False
                return err, False
            else:
                return ret, True
        return new_func
    return decorator
