from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail


mail=Mail()
admin=Admin()
db=SQLAlchemy()
bootstrap=Bootstrap()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)



def create_app(config_name):
    app=Flask(__name__)

    #creating the configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    mail.init_app(app)

    #registering the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    from .admin import admin_view as admin_blueprint
    app.register_blueprint(admin_blueprint,url_prefix='/admin')




    return app
