from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()

from app.models import Usuario

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    bcrypt.init_app(app)

    from app.routes.auth import auth
    from app.routes.main import main
    from app.routes.usuario import usuario
    from app.routes.ticket import ticket
    from app.routes.empresa import empresa

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(usuario)
    app.register_blueprint(ticket)
    app.register_blueprint(empresa)

    return app

