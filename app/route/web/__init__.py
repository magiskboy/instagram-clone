#coding=utf-8

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
from .form import LoginForm
from .form import RegisterForm
from ...service import user as user_service
from ...helper import flash_and_redirect


bp = Blueprint('web', __name__,
               template_folder='templates',
               static_folder='static',
               static_url_path='/static/web')


@bp.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()

    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('web.feed'))
        return render_template('index.jinja2', login_form=login_form)

    if login_form.validate_on_submit():
        ret, success = user_service.get_and_verify_user(**login_form.data)
        if success:
            ret.is_active = True
            login_user(ret)
            return redirect(url_for('web.feed'))
        return flash_and_redirect('web.index', [ret])
    return flash_and_redirect('web.index', login_form.errors.items())


@bp.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.jinja2', register_form=register_form)

    if register_form.validate_on_submit():
        ret, success = user_service.register_user(register_form.data)
        if success:
            return flash_and_redirect('web.index', [f'Please login with {ret.fullname} user'])
        return flash_and_redirect('web.register', [ret])
    return flash_and_redirect('web.register', register_form.errors.items())


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))


@bp.route('/feed')
@login_required
def feed():
    return render_template('feed.jinja2')
