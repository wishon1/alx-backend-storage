#!/usr/bin/env python3
""" module containing a function to list all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """function that lists all documents in a collection

       Args:
        mogo_collection: A pymongo collection object

       Returns: Return an empty list if no document in the collection
    """
    if mongo_collection is None:
        return []

    collection_document = mongo_collection.find()
    return [doc for doc in collection_document]
