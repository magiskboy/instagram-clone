#coding=utf-8

from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask_migrate import Migrate

from .web import create_app as create_web
from .api import create_app as create_api
from ..auth import login_manager
from ..model import db
from ..caching import cache
from ..config import get_config


def create_app(config_name=None):
    app = Flask(__name__)
    config_name = config_name or app.env
    app.config.from_object(get_config(config_name))

    db.init_app(app)
    Migrate(app, db)
    cache.init_app(app)
    login_manager.init_app(app)

    web_app = create_web()
    api_app = create_api()
    web_app.login_manager = login_manager
    api_app.login_manager = login_manager
    app.wsgi_app = DispatcherMiddleware(web_app, mounts={
        '/api': api_app,
    })

    return app
