from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


login= LoginManager()

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    

    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    login.login_view='auth.login'
    login.login_message = "Please Login to access this page."
    login.login_message_category='warning'



    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from .blueprints.social import bp as social_bp
    app.register_blueprint(social_bp)

    return app