#!/usr/bin/env python3
"""select by"""


def schools_by_topic(mongo_collection, topic):
    """return list"""
     topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
