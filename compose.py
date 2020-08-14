#coding=utf-8

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from app.route import web
from app.route import api


web_app = web.create_app()
api_app = api.create_app()

app = DispatcherMiddleware(NotFound(), mounts={
    '/api': api_app,
    '/': web_app,
})
