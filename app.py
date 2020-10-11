import numpy as np
from modelNew import model
import os
import time
import json
from flask import request, make_response
import flask
from flask_cors import cross_origin
app = flask.Flask(__name__)


'''@app.route('/')
def index():
    if request.args:

        context = request.args["context"]
        question = request.args["question"]
        answer =model.predict(context, question)
        return flask.render_template('index.html', question=question, answer=answer['answer'])
    else:
        return flask.render_template('index.html')
        


    return response'''




# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()

def webhook():

    req = request.get_json(silent=True, force=True)

    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# processing the request from dialogflow
def processRequest(req):
    #sessionID=req.get('responseId')
    result = req.get("queryResult")
    #user_says=result.get("queryText")
    #log.write_log(sessionID, "User Says: "+user_says)
    parameters = result.get("parameters")
    context=parameters.get("context")
    question = parameters.get("question")

    intent = result.get("intent").get('displayName')
    
    if (intent=='QA - yes'):
        answer =model.predict(context, question)
    fulfillmentText = "The Iris type seems to be..  {} !".format(answer['answer'])
    return {
            "fulfillmentText": fulfillmentText
        }
    
 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))





