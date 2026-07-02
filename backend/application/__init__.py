from flask import Flask

from application.config import Config
from application.extensions import db, jwt
from application.seed import create_admin


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():

        import application.models

        db.create_all()
        create_admin()
        

    return app