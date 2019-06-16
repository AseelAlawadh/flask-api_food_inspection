import os


class BaseConfig(object):
    TESTING = True
    DEBUG = False

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "food.db"))
    SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass
