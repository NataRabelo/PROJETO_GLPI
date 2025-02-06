from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config import Config
from flask import Flask 

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()

from app.models import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth_bp.login"
    bcrypt.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.ticket import ticket_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(ticket_bp)

    return app