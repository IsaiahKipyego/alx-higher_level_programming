#!/usr/bin/python3
"""
A module containing a function
"""


def inherits_from(obj, a_class):
    """
    checks whether object is an instance of a class that inherited from
    specified class
    """
    if type(obj) is a_class:
        return (False)
    return isinstance(obj, a_class)
