#coding=utf-8

from flask import Blueprint
from flask import render_template
from flask_login import login_required


bp = Blueprint('core', __name__,
               template_folder='templates',
               static_folder='static/core',
               static_url_path='/static/core')


@bp.route('/feed')
@login_required
def feed():
    return render_template('feed.jinja2')
