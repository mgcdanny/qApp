# Import flask and template operators
from flask import Flask
from celery import Celery
#from flask.ext.sqlalchemy import SQLAlchemy


def make_celery(app):
    """Wrapper function for Celery to better integrate with Flask,
    directly from Flask docs"""

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='amqp://rmq',  # rmq is a docker link alias for a running rabbitmq container
    CELERY_RESULT_BACKEND='rpc://',
    CELERY_IMPORTS=('app.tasks',),
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ENABLE_UTC=True,
    CELERY_IGNORE_RESULT=False,
    CELERY_TASK_RESULT_EXPIRES=3600
)

celery = make_celery(app)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_ui.controllers import mod_ui as ui_module
app.register_blueprint(ui_module)



# Define the database object which is imported
# by modules and controllers
# db = SQLAlchemy(app)
# db.create_all()
