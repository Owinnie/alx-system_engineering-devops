#!/usr/bin/python3
from sys import argv
import csv
import json
import requests


if __name__ == "__main__":
    resp = (requests.get('https://jsonplaceholder.typicode.com/todos', params={"userId": argv[1]})).json()
    user = (requests.get('https://jsonplaceholder.typicode.com/users/{}'. format(argv[1]))).json()
    with open(f"{argv[1]}.csv", "w") as cf:
        wtr = csv.writer(cf, quoting=csv.QUOTE_ALL)
        [wtr.writerow(
            [
                argv[1],
                user.get('username'),
                i.get('completed'),
                i.get('title')
            ]
        ) for i in resp]