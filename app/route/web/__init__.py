#coding=utf-8

from flask import Blueprint
from flask import render_template
from .form import LoginForm
from .form import RegisterForm


bp = Blueprint('web', __name__,
                template_folder='templates',
               static_folder='static',
               static_url_path='/static/web')


@bp.route('/')
def index():
    context = {
        'login_form': LoginForm(),
        'register_form': RegisterForm(),
    }
    return render_template('index.jinja2', **context)
