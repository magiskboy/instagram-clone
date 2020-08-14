#coding=utf-8

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask_login import login_required
from ....service import user as user_service


bp = Blueprint('user', __name__,
               template_folder='templates',
               static_folder='static',
               static_url_path='/static/user')


@bp.route('/<string:username>')
@login_required
def userinfo(username):
    user = user_service.get_user(username)
    return render_template('info.jinja2', user=user)
