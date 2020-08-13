#coding=utf-8

from flask import Flask
from flask import jsonify



def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return jsonify(message='Lo con cac')

    return app
