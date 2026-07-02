import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = "trekking-secret-key"
    
    JWT_SECRET_KEY = "trekking-jwt-secret"

    SQLALCHEMY_DATABASE_URI = \
        "sqlite:///" + os.path.join(BASE_DIR, "trekking.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECURITY_PASSWORD_SALT = "trekking-password-salt"

    SECURITY_REGISTERABLE = True

    SECURITY_SEND_REGISTER_EMAIL = False