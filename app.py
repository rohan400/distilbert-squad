from flask import request
import rs
import flask
import os
import time
from threading import Thread


app = flask.Flask(__name__)


@app.route('/')
def hello():
    context ='Telefon mobil Samsung Galaxy A31, Dual SIM, 64GB, 4G, Prism Crush Black  Macro Cam surprinde detaliile din apropiere Camera foto macro de 5MP (40 mm) realizeaza fotografii cu claritate si calitate ridicata, ceea ce te ajuta sa scoti in evidenta detaliile foarte fine ale fotografiilor tale, din apropiere. Aplica si ajusteaza estomparea naturala a fundalului (Bokeh) pentru a izola subiectul si a-i creste impactul vizual. Depth Camera iti aduce subiectul in centrul atentiei'
    question = 'Ce surprinde Macro Cam la Samsung Galaxy A31?'
    answer = rs.predict(context, question)
    return 'Hello World'

'''@app.route('/')

def index():

    if request.args:

        context = request.args["context"]
        question = request.args["question"]
        answer = rs.predict(context, question)
        time.sleep(10)


        return flask.render_template('index.html', question=question, answer=answer)
    else:
        return flask.render_template('index.html')'''





if __name__ == "__main__":
    app.debug = True
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
