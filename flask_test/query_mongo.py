# coding=utf-8
# Copyright 2016, 1 For 1. All Rights Reserved


__author__ = "jiangliubin"
__created__ = "9/18/16"
__license__ = "Commercial. All Rights Reserved."

from pymongo import MongoClient

"""
File Description
"""

MONGOCLIENT = None


def get_client(host='10.0.0.128', port='27017', user=None, password=None):

    try:
        MONGOCLIENT = MongoClient(host=host, port=port)
    except Exception as e:
        return e

    return "succeed"

def get_db(name='twitter'):
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
        return None
    return db


def get_collections(db=None):
    """This function returns all collections in database, need to add more if more collections coming.

    :param db: database.
    :type db: pymongo.database.Database.
    :return collections: all collections in database.
    :rtype collections: dict

    """

    # Collections name
    twitters = db.twitters
    collections = {
        'candidates': twitters,

    }
    return collections


def get_one_document(collection=None, query=None):
    """This function retrieves one document by query.

    :param collection: collection name.
    :type collection: pymongo.collection.Collection.
    :param query: json format, Sample: ({"field_name":value}).
    :type query: dict.
    :return document: the json document from db by query.
    :rtype document: dict.

    """
    try:
        document = collection.find_one(query)

    except Exception as te:
        return None

    return document