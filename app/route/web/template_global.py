#coding=utf-8

def init_app(app):
    # get type name of object
    app.jinja_env.globals.update({'type': lambda x: x.__class__.__name__})
