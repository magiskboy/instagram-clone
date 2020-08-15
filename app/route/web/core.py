#coding=utf-8

import os
from flask import Blueprint
from flask import render_template
from flask_login import login_required


bp = Blueprint('core', __name__,
               template_folder=os.path.join('templates', 'core'))


@bp.route('/feed')
@login_required
def feed():
    return render_template('feed.jinja2')
