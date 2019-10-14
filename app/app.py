import json
import os
import sys
import pickle

import flask
from flask import request, logging
from flask_restplus import Resource, Api, Namespace, reqparse
from flask_cors import CORS, cross_origin

from app.scrape import scrape_main 
from ml.api import *

app = flask.Flask(__name__)
api = Api(app)
CORS(app)
api_namespace = api.namespace("api", description="API for searching for answers to relationship-related queries")

query_args = reqparse.RequestParser()
query_args.add_argument("query", type=str, required=True)
query_args.add_argument("num_results", type=int)

@app.route("/test")
def test():
    return flask.jsonify({"hello":"world"})

@api_namespace.route("/search")
class SearchAPI(Resource):
    @api.expect(query_args, validate=True)
    @api.response(200, "Success")
    @api.response(500, "INTERNAL SERVER ERROR")
    def get(self):
        args = query_args.parse_args()
        query = args["query"]
        num_results = args["num_results"]

        # from scrape/scrape_main.py
        return scrape_main.search_google(query, num_results=num_results)


classifier_args = reqparse.RequestParser()
classifier_args.add_argument("query", type=str, required=True)

vec, model = pickle.load(open("ml/saved/BernoulliNB_7.sav","rb"))

@api_namespace.route("/classify")
class ClassifyAPI(Resource):
    @api.expect(classifier_args, validate=True)
    @api.response(200, "Success")
    @api.response(500, "INTERNAL SERVER ERROR")
    def get(self):
        args = query_args.parse_args()
        query = [args["query"]]

        # from ml folder
        query = get_vectorized_test_x(query, vec)
        pred = int(model.predict(query)[0])

        return {"relationship-related":{1:"yes",0:"no"}[pred]}

@app.after_request
def apply_headers(response):
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

if __name__ == '__main__':  
   app.run(debug=True, port="5000")
