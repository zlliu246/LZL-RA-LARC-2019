import json
import os
import sys

import flask
from flask import request
from flask_cors import CORS

from app.scrape import scrape_main 

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

if __name__ == '__main__':  
   app.run(debug=True, port="5000")
