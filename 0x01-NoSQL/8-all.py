#!/usr/bin/env python3
"""list all doc nosql"""


from pprint import pprint


def list_all(mongo_collection):
    """return empty if not doc"""
    school = mongo_collection.find()
    if school.count() == 0:
        return []
    for doc in school:
        return [doc]
