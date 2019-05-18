from flask import Blueprint

api = Blueprint('api', __name__)

from app.financas.api import routes