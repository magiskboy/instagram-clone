#coding=utf-8

import os
import secrets
from sqlalchemy.engine.url import URL


class BaseConfig:
    ROOT = os.getcwd()

    TESTING = False

    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = secrets.token_hex(16)


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BaseConfig.ROOT, "db.sqlite3")}'

    SECRET_KEY = '0'*16


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    _url = URL('mysql+pymysql', os.getenv('DB_USER'), os.getenv('DB_PASS'), os.getenv('DB_HOST'),
               os.getenv('DB_PORT', 3306), os.getenv('DB_NAME', 'instagram_clone'))
    SQLALCHEMY_DATABASE_URI = str(_url)


def get_config(name):
    return {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
    }.get(name, 'production')
