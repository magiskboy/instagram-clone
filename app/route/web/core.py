#coding=utf-8

from flask import Blueprint
from flask import render_template


bp = Blueprint('core', __name__,
               template_folder='templates',
               static_folder='static/core',
               static_url_path='/static/core')


@bp.route('/feed')
def feed():
    return render_template('core/feed.jinja2')
