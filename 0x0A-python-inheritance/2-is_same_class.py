#!/usr/bin/python3
"""
module that contains a function
"""


def is_same_class(obj, a_class):
    """
    checks whether an object is exactly an instance of a class
    """
    return type(obj) is a_class
