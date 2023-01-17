#!/usr/bin/env python3
"""list all doc nosql"""


import pymongo


def list_all(mongo_collection):
    """return empty if not doc"""
    school = mongo_collection.find()
    if not mongo_collection:
        return []
    for doc in school:
        return [doc]
