from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from elwasfa.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from elwasfa.users.routes import users
    from elwasfa.recipes.routes import recipes
    from elwasfa.main.routes import main
    from elwasfa.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(recipes)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app