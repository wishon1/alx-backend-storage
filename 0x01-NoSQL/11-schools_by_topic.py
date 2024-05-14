#!/usr/bin/env python3
"""This Python function retrieves a list of schools that cover a
specific topic.

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection refers to the pymongo collection object
topic (string) is the topic being searched
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """Retrieves a list of schools covering a specific topic."""
    return mongo_collection.find({"topics": topic})
