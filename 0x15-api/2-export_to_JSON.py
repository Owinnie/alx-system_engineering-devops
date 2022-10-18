#!/usr/bin/python3
"""To JSON Style"""
from sys import argv
import csv
import json
import requests


if __name__ == "__main__":
    resp = (requests.get('https://jsonplaceholder.typicode.com/todos', params={"userId": argv[1]})).json()
    user = (requests.get('https://jsonplaceholder.typicode.com/users/{}'. format(argv[1]))).json()
    with open(f"{argv[1]}.json", "w") as jf:
        json.dump(
            {
                argv[1]: [
                    {
                        "task": i.get('title'),
                        "completed": i.get('completed'),
                        "username": user.get('username')
                    }
                    for i in resp
                ]
            },
            jf
        )
