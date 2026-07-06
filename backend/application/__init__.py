from flask import Flask

from application.config import Config
from application.extensions import db, jwt
from application.seed import create_admin
from application.routes.auth import auth_bp
from application.routes.admin import admin_bp
from application.routes.staff import staff_bp
from application.routes.trekker import trekker_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():

        import application.models

        db.create_all()
        create_admin()

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(trekker_bp)

    return app