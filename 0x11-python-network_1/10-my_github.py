#!/usr/bin/python3
"""
takes github credentials and uses git api to display your id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    if len(argv) > 2:
        user = argv[1]
        token = argv[2]
        auth = HTTPBasicAuth(user, token)
        r = requests.get(url, auth=auth)
        id = r.json().get("id")
        print(id)
