#!/usr/bin/python3
"""
A module returning a list of available attributes and methods of an object
"""


def lookup(obj):
    """
    returns list of available attributes and methods of an object
    """
    return (dir(obj))
