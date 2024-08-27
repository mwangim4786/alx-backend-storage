#!/usr/bin/env python3
""" MongoDB in  Python using pymongo """

def list_all(mongo_collection):
    """ lists all documents in a collection: """
    all_docs = mongo_collection.find()

    if all_docs.count() == 0:
        return []

    return all_docs
