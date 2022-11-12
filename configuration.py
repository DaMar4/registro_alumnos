import secrets
class Config(object):
    SECRET_KEY = secrets.token_urlsafe(64)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:2909@127.0.0.1:5432/dbAlumnos'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
class DevelopmentConfig(Config):
    'Configuracion de desarrollo'
    DEBUG = True
    TESTING = True
    SECREY_KEY = 'tienda'