from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from .base import bp as base_bp
    app.register_blueprint(base_bp, url_prefix="/base")

    from .main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/")

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from .workout import bp as workout_bp
    app.register_blueprint(workout_bp, url_prefix="/workout")

    return app

from . import models