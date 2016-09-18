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
    try:
        client = query_mongo.get_client()
    except:
        return "error call client function"
    return client
    # return flask.render_template('index.html')

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
