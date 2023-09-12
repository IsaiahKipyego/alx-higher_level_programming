#!/usr/bin/python3
"""
A module returning dictionary description with simple data struc
"""


def class_to_json(obj):
    """
    returns dictionary description with simple data structure
    Args:
        obj: class instance
    Return:
        dictionary description
    """
    dictionary = {}
    if hasattr(obj, "__dict__"):
        dictionary = obj.__dict__.copy()
    return dictionary
