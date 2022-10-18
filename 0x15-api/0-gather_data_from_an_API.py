#!/usr/bin/python3
from sys import argv
import csv
import json
import requests


if __name__ == "__main__":
    resp = (requests.get('https://jsonplaceholder.typicode.com/todos', params={"userId": argv[1]})).json()
    user = (requests.get('https://jsonplaceholder.typicode.com/users/{}'. format(argv[1]))).json()
    done = [i.get('title') for i in resp if i.get('completed') == True]
    print(f"Employee {user.get('name')} is done with tasks {len(done)}/{len(resp)}")
    [print(f"\t {tsk}") for tsk in done]