#coding=utf-8

from sqlalchemy import Column
from sqlalchemy import TIMESTAMP
from sqlalchemy import Integer
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class BaseModel:
    id_ = Column(Integer(), primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP(), default=func.now())
    updated_at = Column(TIMESTAMP(), onupdate=func.now(), default=None)


    def save(self):
        db.session.add(self)
        db.session.commit()


    def flush(self):
        db.session.add(self)
        db.session.flush()
