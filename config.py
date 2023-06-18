import os


secret_key = os.urandom(24).hex()
class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secret_key
    DB_URI = "postgresql://qkckiumm:QVSo78otyZOwpjbWUwVSL8ejB-udjOep@silly.db.elephantsql.com/qkckiumm"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.DB_URI

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = Config.DB_URI

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
