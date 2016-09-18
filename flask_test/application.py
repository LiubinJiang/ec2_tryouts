# coding=utf-8

__author__ = "Izzy"
__created__ = "9/17/16"
__license__ = "All Rights Reserved."

from flask import Flask

"""
File Description
"""

application = Flask(__name__)

@application.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
