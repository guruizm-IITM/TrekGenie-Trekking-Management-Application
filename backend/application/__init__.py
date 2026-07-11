from flask import Flask
from application.config import Config
from application.seed import create_admin
from application.routes.auth import auth_bp
from application.routes.admin import admin_bp
from application.routes.staff import staff_bp
from application.routes.trekker import trekker_bp
from application.extensions import db, jwt, cors, cache, celery


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.config["CACHE_TYPE"] = "RedisCache"

    app.config["CACHE_REDIS_URL"] = "redis://localhost:6379/0"

    app.config["CACHE_DEFAULT_TIMEOUT"] = 300

    cache.init_app(app)

    celery.conf.update(
        broker_url="redis://localhost:6379/0",
        result_backend="redis://localhost:6379/0",
        timezone="Asia/Kolkata",
        enable_utc=False,
        imports=("application.tasks",),
    )

    db.init_app(app)
    jwt.init_app(app)

    cors.init_app(
        app,
        resources={
            r"/*": {
                "origins": "http://localhost:5173"
            }
        }
    )

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