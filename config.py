import os

class Config:
    """
    general configurations
    """

    SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    production configuration, child class

    args:
    confi:the parent class
    '''

class DevConfig(Config):
    '''
    development configuration, child class

    args:
    confi:the parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://chutha:chutha@localhost/writers_platform'

    debug=True

config_options={
'development':DevConfig,
'production':ProdConfig
}
