import os

class Config:
    """
    general configurations
    """

    SECRET_KEY=os.environ.get('SECRET_KEY')
        #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'tutorials platform'
    SENDER_EMAIL = 'njorogedavid13@gmail.com'


class ProdConfig(Config):
    '''
    production configuration, child class

    args:
    confi:the parent class
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    development configuration, child class

    args:
    confi:the parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://chutha:chutha@localhost/writers_platform'

    DEBUG=True

config_options={
'development':DevConfig,
'production':ProdConfig
}
