from flask import Blueprint

auth = Blueprint('auth', __name__)

from app.financas.auth import routes