#!/usr/bin/python3
"""
takes url, sends a request to url and displays values
of X-Request-Id
"""
from sys import argv
from urllib import request
if len(argv) > 1:
    with request.urlopen(request.Request(argv[1])) as response:
        for key, value in response.headers.items():
            if key == 'X-Request-Id':
                print(value)
