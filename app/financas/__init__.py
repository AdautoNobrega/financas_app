import logging
import os
from logging.handlers import RotatingFileHandler, SMTPHandler

from flask import Flask, current_app, request

from app.financas.models import Base, MySession
from config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

# from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder="./dist/static",
                template_folder="./dist")
    app.config.from_object(config_class)
    app.secret_key = 'SECRET'
    app.config['SECRET_KEY'] = 'SECRET'
    app.config['SESSION_TYPE'] = 'filesystem'

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    Session(app)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.debug = True
    app.use_reloader = True
    mysession = MySession(Base)
    app.config['dbsession'] = mysession.session

    from app.financas.main import bp as main_bp
    from app.financas.auth import auth as auth_bp
    from app.financas.api import api as api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')

    app.logger.setLevel(logging.INFO)
    app.logger.info('Finance app startup')

    return app
