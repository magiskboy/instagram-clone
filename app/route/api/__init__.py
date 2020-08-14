#coding=utf-8

from flask import Flask
from flask import jsonify
from flask_login import LoginManager
from ..config import get_config
from ...model import db
from ...model import UserModel


login_manager = LoginManager()
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


    @app.route('/ping')
    def index():
        return jsonify(message='pong')

    return app
