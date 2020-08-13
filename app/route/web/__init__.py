#coding=utf-8

from flask import Flask
from . import template_global
from .core import bp as core_bp
from .auth import bp as auth_bp


def create_app(config_name=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a' * 16

    app.register_blueprint(core_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
