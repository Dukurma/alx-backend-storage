#!/usr/bin/env python3
"""NoSQL with pymongo"""
from pymongo import MongoClient
from collections import Counter
""" Python script that provides some stats about
    Nginx logs stored in MongoDB """

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx

    print("{} logs".format(nginx_logs.count_documents({})))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_logs.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = nginx_logs.count_documents({"method": "GET",
                                               "path": "/status"})
    print("{} status check".format(status_check))

    print("IPs:")
    all_ips = Counter(log["ip"] for log in nginx_logs.find())
    for ip, count in all_ips.most_common(10):
        print(f"\t{ip}: {count}")
