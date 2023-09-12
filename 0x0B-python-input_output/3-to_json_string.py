#!/usr/bin/python3
"""
A module with function returning the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    Returns json representation of an object
    Args:
        my_obj: string to convert to JSON representation
    """
    return (json.dumps(my_obj))
