import os

class Config:
    """
    general configurations
    """

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
    debug=True

config_options={
'development':DevConfig,
'production':ProdConfig
}
