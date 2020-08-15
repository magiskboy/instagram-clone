#coding=utf-8

import os
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user
from .form.auth import LoginForm
from .form.auth import RegisterForm
from ...service import user as user_service
from ...helper import flash_and_redirect


bp = Blueprint('auth', __name__,
               template_folder=os.path.join('templates', 'auth'))


@bp.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()

    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('core.feed'))
        return render_template('index.jinja2', login_form=login_form)

    if login_form.validate_on_submit():
        ret, success = user_service.get_user(**login_form.data, verify=True)
        if success:
            ret.is_active = True
            login_user(ret)
            return redirect(url_for('core.feed'))
        return flash_and_redirect('auth.index', [ret])
    return flash_and_redirect('auth.index', login_form.errors.items())


@bp.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.jinja2', register_form=register_form)

    if register_form.validate_on_submit():
        ret, success = user_service.register_user(register_form.data)
        if success:
            return flash_and_redirect('auth.index', [f'Please login with {ret.fullname} user'])
        return flash_and_redirect('auth.register', [ret])
    return flash_and_redirect('auth.register', register_form.errors.items())


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))
