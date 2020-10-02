import numpy as np
from flask import Flask, request, make_response
from flask_cors import cross_origin
import rs
import threading


from concurrent.futures import ThreadPoolExecutor
from time import sleep
# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
executor = ThreadPoolExecutor(2)

app = Flask(__name__)


@app.route('/')
def run_jobs():
    executor.submit(someHeavyFunction)
    return 'One job were launched in background!'



def someHeavyFunction():
    context = "Telefon mobil Samsung Galaxy A31, Dual SIM, 64GB, 4G, Prism Crush Black  Macro Cam surprinde detaliile din apropiere Camera foto macro de 5MP (40 mm) realizeaza fotografii cu claritate si calitate ridicata, ceea ce te ajuta sa scoti in evidenta detaliile foarte fine ale fotografiilor tale, din apropiere. Aplica si ajusteaza estomparea naturala a fundalului (Bokeh) pentru a izola subiectul si a-i creste impactul vizual. Depth Camera iti aduce subiectul in centrul atentiei"
    question = "Ce surprinde Macro Cam la Samsung Galaxy A31?"
    sleep(10)
    answer = rs.predict(context, question)
    print(answer)
    return answer



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))




