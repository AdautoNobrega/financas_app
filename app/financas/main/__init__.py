from flask import Blueprint

bp = Blueprint('main', __name__)

from app.financas.main import routes
