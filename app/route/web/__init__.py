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
from .form import LoginForm
from .form import RegisterForm
from ...service import user as user_service


bp = Blueprint('web', __name__,
                template_folder='templates',
               static_folder='static',
               static_url_path='/static/web')


@bp.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            user = user_service.get_and_verify_user(
                login_form.username.data,
                login_form.password.data
            )
            if user:
                login_user(user)
                return redirect(url_for('web.feed'))
            flash(('', 'Username or password is wrong'), 'error')
            return redirect(url_for('web.index'))
        for error in login_form.errors.items():
            flash(error, 'error')
        return redirect(url_for('web.index'))

    context = {
        'login_form': login_form,
    }
    return render_template('index.jinja2', **context)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    context = {
        'register_form': RegisterForm()
    }
    return render_template('register.jinja2')


@bp.route('/logout')
@login_required
def logout():
    logout_user()


@bp.route('/feed')
@login_required
def feed():
    return 'Feed'
