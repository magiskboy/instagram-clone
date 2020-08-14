#coding=utf-8

from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from app.route import web
from app.route import api


web_app = web.create_app()
api_app = api.create_app()

app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(web_app, mounts={
    '/api': api_app
})
