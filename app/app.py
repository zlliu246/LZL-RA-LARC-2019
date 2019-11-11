import json
import os
import sys
import pickle

import flask
from flask import request
from flask_cors import CORS

from app.scrape import scrape_main 
from ml.api import *

app = flask.Flask(__name__)
CORS(app)

@app.route("/")
def home_():
    return """
        /api/query?query={query}&num_results={num_results} <br/>
            returns {num_results} top results from query, ranked by frequency of keywords in response <br/>

        <br/>
        /api/classify?query={query}&num_results={num_results} <br/>
            predicts whether a question is relationship related based on pre-trained model <br/>

    """

@app.route("/api/query")
def query_():
    args = request.args
    query = args["query"]
    num_results = int(args.get("num_results",3))

    """
        from app/scrape/scrape_main.py
    """
    return flask.jsonify(scrape_main.search_google(query, num_results=num_results))

vec, model = pickle.load(open("ml/saved/BernoulliNB_7.sav","rb"))

@app.route("/api/classify")
def classify_():
    args = request.args
    raw_query = args["query"]

    query = get_vectorized_test_x([raw_query], vec)
    pred = int(model.predict(query)[0])

    return flask.jsonify({
        "query": raw_query,
        "relationship-related":{1:"yes", 0:"no"}[pred]
    })

if __name__ == '__main__':  
   app.run(debug=True, port="5000")
