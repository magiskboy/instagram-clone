#coding=utf-8

import os
import secrets
from sqlalchemy.engine.url import URL


SECRET_KEY_LEN = 16


class BaseConfig:
    ROOT = os.getcwd()

    TESTING = False

    DEBUG = False

    _url = URL('mysql+pymysql', os.getenv('DB_USER'), os.getenv('DB_PASS'), os.getenv('DB_HOST'),
               os.getenv('DB_PORT', 3306), os.getenv('DB_NAME', 'instagram_clone'))
    SQLALCHEMY_DATABASE_URI = str(_url)

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = secrets.token_hex(SECRET_KEY_LEN)


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    SECRET_KEY = '0' * SECRET_KEY_LEN


class TestingConfig(BaseConfig):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(BaseConfig):
    pass


def get_config(name):
    return {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
    }.get(name, 'production')
