#coding=utf-8

import os
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask_login import login_required
from ...helper import flash_and_redirect
from ...service import user as user_service
from .form.user import UpdatePersonalPageForm


bp = Blueprint('user', __name__,
               template_folder=os.path.join('templates', 'user'))


@bp.route('/<string:username>')
@login_required
def userinfo(username):
    user, n_friends, n_followers = user_service.get_personal_info(username)
    return render_template('info.jinja2',
                           user=user,
                           n_friends=n_friends,
                           n_followers=n_followers)


@bp.route('/edit', methods=['GET', 'POST'])
def update_personal_page():
    form = UpdatePersonalPageForm()
    if request.method == 'GET':
        return render_template('update_personal_page.jinja2', form=form)

    if form.validate_on_submit():
        pass
    return flash_and_redirect('user.update_personal_page', ['Update failure'])
