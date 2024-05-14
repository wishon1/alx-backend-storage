#!/usr/bin/env python3
"""
A Python script for providing statistical insights into Nginx logs stored
in MongoDB:

Database: logs
Collection: nginx
Display (similar to the example):
first line: x logs indicating the number of documents in this collection
second line: Methods:
5 lines indicating the count of documents with the method =
["GET", "POST", "PUT", "PATCH", "DELETE"] respectively
(one tabulation before each line)
one line indicating the count of documents with:
method=GET
path=/status
You can utilize the provided dump as a data sample: dump.zip
"""

import pymongo
from pymongo import MongoClient


def log_nginx_stats(mongo_collection):
    """Provides statistical insights into Nginx logs."""
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    number_of_gets = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{number_of_gets} status check")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_nginx_stats(mongo_collection)
