from flask import request
import rs
from celery import Celery
from datetime import timedelta
import os
import time


def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

app = flask.Flask(__name__)
app.config['CELERY_BACKEND'] = "redis://redis:6379/0"
app.config['CELERY_BROKER_URL'] = "redis://redis:6379/0"

app.config['CELERYBEAT_SCHEDULE'] = {
    'say-every-5-seconds': {
        'task': 'return_something',
        'schedule': timedelta(seconds=5)
    },
}
app.config['CELERY_TIMEZONE'] = 'UTC

celery_app = make_celery(app)

@celery_app.task(name='return_something')
def return_something():
    if request.args:

        context = request.args["context"]
        question = request.args["question"]
        answer = rs.predict(context, question)



        return flask.render_template('index.html', question=question, answer=answer)
    else:
        return flask.render_template('index.html')

@app.route('/')
def home():
    result = return_something.delay()
    return result.wait()





