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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))




