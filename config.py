import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    SECRET_KEY = 'very-very-secret'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    MAILER_SMTP = os.environ['MAILER_SMTP']
    MAIL_SECRET_KEY = os.environ['MAIL_SECRET_KEY']
    MAILER_PORT = 587
<

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
