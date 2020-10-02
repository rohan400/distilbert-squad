from flask import request
import rs
import flask
import os
import time
import logging


from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
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



app.config.update(
    CELERY_BROKER_URL='0.0.0.0:8080',
    CELERY_RESULT_BACKEND='0.0.0.0:8080'
)
celery = make_celery(app)


@celery.task()
def index():
    if request.args:

        context = request.args["context"]
        question = request.args["question"]
        rs.load_model()
        answer = rs.predict(context, question)
        time.sleep(10)


        return flask.render_template('index.html', question=question, answer=answer)
    else:
        return flask.render_template('index.html')





'''if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))'''
