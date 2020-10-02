from flask import request
import rs
import flask
import os
import time
import logging


app = flask.Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)



@app.route('/', methods=['GET', 'POST'])

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





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
