from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
# from flask_cors import CORS

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder="./dist/static",
                template_folder="./dist")
    app.config.from_object(config_class)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.debug = True
    app.use_reloader = True
    db.init_app(app)

    from app.financas.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
