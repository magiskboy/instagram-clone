#coding=utf-8

from flask import Blueprint
from flask import jsonify


bp = Blueprint('api', __name__)


@bp.route('/')
def index():
    return jsonify(message='Lo con cac')
