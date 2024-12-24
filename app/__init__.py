from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from .routes.auth import auth_bp
    from .routes.user import user_bp
    from .routes.test import test_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(test_bp)

    return app
