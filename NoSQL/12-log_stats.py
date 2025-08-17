#!/usr/bin/env python3
"""
Script to display statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # total of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
