import numpy as np
from flask import Flask, request, make_response
from flask_cors import cross_origin
import rs
'''import threading


from concurrent.futures import ThreadPoolExecutor
from time import sleep
# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
executor = ThreadPoolExecutor(1)

app = Flask(__name__)


@app.route('/')
def run_jobs():
    future=executor.submit(someHeavyFunction)
    return_value = future.result()
    return return_value



def someHeavyFunction():
    context = "Telefon mobil Samsung Galaxy A31, Dual SIM, 64GB, 4G, Prism Crush Black  Macro Cam surprinde detaliile din apropiere Camera foto macro de 5MP (40 mm) realizeaza fotografii cu claritate si calitate ridicata, ceea ce te ajuta sa scoti in evidenta detaliile foarte fine ale fotografiilor tale, din apropiere. Aplica si ajusteaza estomparea naturala a fundalului (Bokeh) pentru a izola subiectul si a-i creste impactul vizual. Depth Camera iti aduce subiectul in centrul atentiei"
    question = "Ce surprinde Macro Cam la Samsung Galaxy A31?"
    answer = rs.predict(context, question)
    print(answer)
    return answer'''

from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/')
def run_jobs():
    task = my_background_task.apply_async(countdown=20)
    return task

@celery.task
def my_background_task():
    # some long running task here
    context = "Telefon mobil Samsung Galaxy A31, Dual SIM, 64GB, 4G, Prism Crush Black  Macro Cam surprinde detaliile din apropiere Camera foto macro de 5MP (40 mm) realizeaza fotografii cu claritate si calitate ridicata, ceea ce te ajuta sa scoti in evidenta detaliile foarte fine ale fotografiilor tale, din apropiere. Aplica si ajusteaza estomparea naturala a fundalului (Bokeh) pentru a izola subiectul si a-i creste impactul vizual. Depth Camera iti aduce subiectul in centrul atentiei"
    question = "Ce surprinde Macro Cam la Samsung Galaxy A31?"
    rs.load_model()
    answer = rs.predict(context, question)
    print(answer)
    return answer




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))




