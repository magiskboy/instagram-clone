#coding=utf-8

from flask import Flask
from flask_migrate import Migrate
from ..config import get_config
from ..model import db
from ..auth import login_manager
from ..caching import cache
from . import web
from .web import template_global
from . import api


def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name or app.env))


    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
    cache.init_app(app)
    template_global.init_app(app)

    app.register_blueprint(web.bp, url_prefix='/')
    app.register_blueprint(api.bp, url_prefix='/api')

    return app
