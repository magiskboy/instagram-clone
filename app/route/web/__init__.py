#coding=utf-8

from secrets import token_hex
from flask import Flask
from flask_login import LoginManager
from . import template
from ...model import UserModel
from ...model import db
from ..config import get_config

from .auth import bp as auth_bp
from .core import bp as core_bp
from .user import bp as user_bp


login_manager = LoginManager()
login_manager.login_view = 'auth.index'
@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)



def create_app(config_name=None):
    global login_manager
    global cache

    app = Flask(__name__)
    config = get_config(config_name or app.env)
    app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)
    template.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(core_bp, url_prefix='/')
    app.register_blueprint(user_bp, url_prefix='/users')

    return app
