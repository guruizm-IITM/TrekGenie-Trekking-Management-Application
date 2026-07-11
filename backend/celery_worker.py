from celery import Celery

from application import create_app


app = create_app()


celery = Celery(

    "trekking",

    broker="redis://localhost:6379/0",

    backend="redis://localhost:6379/0",

    include=[

        "application.tasks"

    ]

)

celery.conf.timezone = "Asia/Kolkata"

celery.conf.enable_utc = False


class ContextTask(celery.Task):

    def __call__(self, *args, **kwargs):

        with app.app_context():

            return self.run(*args, **kwargs)


celery.Task = ContextTask