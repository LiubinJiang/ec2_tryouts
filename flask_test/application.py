# coding=utf-8

__author__ = "Izzy"
__created__ = "9/17/16"
__license__ = "All Rights Reserved."

import flask
from flask import Flask
import query_mongo

"""
File Description
"""

application = Flask(__name__)

@application.route("/index.html")
def display():
    client = query_mongo.get_client()
    if not client:
        return "Can't find client"
    else:
        return "client found"
    # return flask.render_template('index.html')

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
