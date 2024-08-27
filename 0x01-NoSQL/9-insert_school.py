#!/usr/bin/env python3
""" MongoDB in  Python using pymongo """

def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs: """
    doc = mongo_collection.insert(kwargs)
    return doc
