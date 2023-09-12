#!/usr/bin/python3
"""
A module converting json file content to python object
"""


import json


def load_from_json_file(filename):
    """
    reads json file and converts contents to python object
    Args:
        filename: the name of file to convert
    """
    with open(filename, encoding="utf-8") as file_open:
        text_obj = json.loads(file_open.read())
        return (text_obj)
