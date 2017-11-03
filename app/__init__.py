from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

db=SQLAlchemy()
bootstrap=Bootstrap()



def create_app(config_name):
    app=Flask(__name__)

    #creating the configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    #registering the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
