#!/usr/bin/env python3
""" MongoDB in  Python using pymongo """

def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name: """
    query_id = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query_id, new_values)
