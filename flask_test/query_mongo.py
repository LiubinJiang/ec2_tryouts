# coding=utf-8
# Copyright 2016, 1 For 1. All Rights Reserved


__author__ = "jiangliubin"
__created__ = "9/18/16"
__license__ = "Commercial. All Rights Reserved."

from pymongo import MongoClient
from bson.objectid import ObjectId

"""
File Description
"""

MONGOCLIENT = None


def get_client(host='localhost', port=27017, user=None, password=None):

    try:
        MONGOCLIENT = MongoClient(host=host, port=port)
    except Exception as e:
        return "get Mongo Client error"

    print "succeed"
    return MONGOCLIENT


def get_db(name='twitters'):
    """This function returns the database for the current application.

    :param name: database name.
    :type name: str.
    :return db: database.
    :rtype db: pymongo.database.Database.

    """
    try:
        client = get_client()
        db = client.get_database(name)
    except Exception as e:
        return "get DB error"

    return db


def get_one_result(db=None):

    # Collections name
    twitter_sentiments = db.twitter_sentiments
    document = twitter_sentiments.find_one({'_id': ObjectId('57defa98aa513c46932bb992')})

    if document:
        print "get document"
        print document
        print document.get('text')
        return document.get('text')

    return None
#
#
# def get_one_document(collection=None, query=None):
#     """This function retrieves one document by query.
#
#     :param collection: collection name.
#     :type collection: pymongo.collection.Collection.
#     :param query: json format, Sample: ({"field_name":value}).
#     :type query: dict.
#     :return document: the json document from db by query.
#     :rtype document: dict.
#
#     """
#     try:
#         document = collection.find_one(query)
#
#     except Exception as te:
#         return None
#
#     return document