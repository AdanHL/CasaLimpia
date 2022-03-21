import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from app.models import UserModel

login_manager = LoginManager()

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    app = Flask(__name__)

    bootstrap = Bootstrap(app)

    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'org.sqlite'),
    )

    login_manager.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from .auth import auth
    app.register_blueprint(auth)
    
    return app