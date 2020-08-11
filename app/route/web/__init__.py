#coding=utf-8

from flask import Blueprint
from flask import render_template


bp = Blueprint('web', __name__,
                template_folder='templates',
               static_folder='static',
               static_url_path='/static/web')


@bp.route('/')
def index():
    return render_template('index.jinja2')
