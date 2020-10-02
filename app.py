import numpy as np
from flask import Flask, request, make_response
import json
import pickle
from flask_cors import cross_origin
import rs

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    result = req.get("queryResult")
    #user_says=result.get("queryText")
    #log.write_log(sessionID, "User Says: "+user_says)
    parameters = result.get("parameters")
    context=parameters.get("context")
    question = parameters.get("question")

    
    if (intent=='QA - yes'):
        prediction = rs.predict(context,question)
    
       
        fulfillmentText= "The Iris type seems to be..  {} !".format(prediction)
        #log.write_log(sessionID, "Bot Says: "+fulfillmentText)
        return {
            "fulfillmentText": fulfillmentText
        }


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))




