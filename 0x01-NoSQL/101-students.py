#!/usr/bin/env python3
""" MongoDB in  Python using pymongo """

def top_students(mongo_collection):
    """  """
    sort_std = mongo_collection.aggregate([
	{
		"$project" : {
			"name" : 1,
			"averageScore" : {"$avg": "$topics.score"}
		}
	},

	{"$sort" : {"averageScore" : -1}}

    ])

    return sort_std
