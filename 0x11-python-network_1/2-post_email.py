#!/usr/bin/python3
"""
takes url and send post request with email as paramenter
displays body of the response
"""
from urllib import request, parse
from sys import argv

if len(argv) > 2:
    url = argv[1]
    email = argv[2]
    value = {'email': email}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
