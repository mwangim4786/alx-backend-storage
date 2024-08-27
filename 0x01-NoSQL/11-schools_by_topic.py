#!/usr/bin/env python3
""" MongoDB in  Python using pymongo """

def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic: """
    docs = mongo_collection.find({"topics": topic})
    list_docs = [doc for doc in docs]
    return list_docs
