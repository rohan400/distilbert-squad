import numpy as np
from flask import Flask, request, make_response, Response
from flask_cors import cross_origin
import rs
import os
import time
import json
from datetime import datetime, timedelta
app = Flask(__name__)

'''@app.route('/')
def hello():
    context = "Telefon mobil Samsung Galaxy A31, Dual SIM, 64GB, 4G, Prism Crush Black  Macro Cam surprinde detaliile din apropiere Camera foto macro de 5MP (40 mm) realizeaza fotografii cu claritate si calitate ridicata, ceea ce te ajuta sa scoti in evidenta detaliile foarte fine ale fotografiilor tale, din apropiere. Aplica si ajusteaza estomparea naturala a fundalului (Bokeh) pentru a izola subiectul si a-i creste impactul vizual. Depth Camera iti aduce subiectul in centrul atentiei"
    question = "Ce surprinde Macro Cam la Samsung Galaxy A31?"
    response = Response(rs.predict(context, question))
    time.sleep(10)
    
    @response.call_on_close
    def on_close():
        for i in range(10):
            sleep(1)
            print(i)

    return response'''
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


# extended time by 3 sec to make condition which is execute before webhook deadline occur:
extended_time = now + timedelta(seconds=3)


@app.route('/')
def hello():
    return 'Hello World'

# geting and sending response to dialogflow
'''@app.route('/webhook', methods=['POST'])
@cross_origin()

def webhook():

    req = request.get_json(silent=True, force=True)

    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=2)
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
        #response = Response(rs.predict(context, question))
        if now<=extended_time:
            fulfillmentText = 'Typing...'
            time.sleep(3.5)
        reply={
                "followupEventInput": {
                        "name": "extent_webhook_deadline",
                        "languageCode": "en-US"
                    }
            }

    if (intent=='QA - yes - custom'):
        if now<=extended_time:
            fulfillmentText = 'Typing...'
            time.sleep(3.5)
        reply={
                "followupEventInput": {
                        "name": "extent_webhook_deadline2",
                        "languageCode": "en-US"
                    }
            }
                
    if (intent=='QA - yes - custom - custom'):
        if now<=extended_time:
            time.sleep(3.5)

    fulfillmentText = "The Iris type seems to be..  {} !".format(response)
    return {
            "fulfillmentText": fulfillmentText
        }
    
 '''      
    req = request.get_json(silent=True, force=True)

    intent = result.get("intent").get('displayName')
    reply=''
    if intent=='QA - yes ':

        # Added time delay to fail the below 'if condition' of normal response for welcome intent:
        time.sleep(3.5)
        
        # if current time is less than or equal to extended time then only below condition becomes "True":
        if now<=extended_time:
            # make a webhook response for welcome intent:
            reply={ "fulfillmentText": "This is simple welcome response from webhook",
                    "fulfillmentMessages": [
                            {
                            "text": {
                                    "text": [
                                        "This is simple welcome response from webhook"
                                    ]
                                }
                            }
                        ],  
                }

        # Create a Followup event when above "if condition" fail:
        reply={
                "followupEventInput": {
                        "name": "extent_webhook_deadline",
                        "languageCode": "en-US"
                    }
            }

    # Create a chain of followup event. Enter into first follow up event:
    # second intent action:

    if (intent=='QA - yes - custom'):
        print("enter into first followup event")

        # Added time delay to fail the below 'if condition' and extend time by "3.5 sec", means right now total time "7 seconds" after webhook execute:
        time.sleep(3.5)
        
        # if current time is less than or equal to extended time then only below condition becomes "True": 
        if now<=extended_time:
            reply={ "fulfillmentText": "Yea, hi there. this is followup 1 event response for webhook.",
                    "fulfillmentMessages": [
                            {
                            "text": {
                                    "text": [
                                        "Yea, hi there. this is followup 1 event response for webhook."
                                    ]
                                }
                        }
                    ],
                "languageCode": "en",
            }

        # Create a Followup event number 2 when above "if condition" fail:
        reply={
                "followupEventInput": {
                        "name": "extent_webhook_deadline_2",
                        "languageCode": "en-US"
                    }
            }
    
    # Third intent action: 
    if (intent=='QA - yes - custom - custom'):
        print("enter into second followup event")

        # Added time delay to fail the below condition and extended more time by "3.5 sec", means right now total time "10.5 seconds" after webhook execute:
        time.sleep(3.5)
        
        # below response should be generated for extended webhook deadline:
        reply={ "fulfillmentText": "Yea, hi there. this is followup event 2 response for webhook.",
                    "fulfillmentMessages": [
                            {
                            "text": {
                                    "text": [
                                        "Yea, hi there. this is followup event 2 response for webhook."
                                    ]
                                }
                            }
                        ],
                "languageCode": "en",
            }
        
        print("Final time of execution:=>", now.strftime("%H:%M:%S"))
    return reply
@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():

    # return response
    return make_response(jsonify(broadbridge_webhook_results()))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))




