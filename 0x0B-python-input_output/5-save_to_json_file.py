#!/usr/bin/python3
"""
A module writing an object into a file as json string
"""


import json


def save_to_json_file(my_obj, filename):
    """
    A function saves an object in a json file
    Args:
        my_obj: object to write to file
        filename: name of file to write
    """
    with open(filename, "w", encoding="utf-8") as file_open:
        file_open.write(json.dumps(my_obj))
