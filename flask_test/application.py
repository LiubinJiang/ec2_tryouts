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
        db = query_mongo.get_db()
        result = query_mongo.get_one_result(db)
    except:
        return "error call search or db or client function"
    return result
    # return flask.render_template('index.html')

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
