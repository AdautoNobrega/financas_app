import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder = "./dist/static", template_folder = "./dist")
    app.config.from_object(config_class)    
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    
    return app

from app.financas import models
