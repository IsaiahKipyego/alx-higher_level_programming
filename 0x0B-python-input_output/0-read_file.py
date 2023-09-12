#!/usr/bin/python3
"""
A module containing a function reading a given file
"""


def read_file(filename=""):
    """
    reads given file passed as parameter
    Args:
        filename: name of the file to be read
    prints the file contents into stdout
    """
    with open(filename, encoding="utf-8") as file_open:
        text = file_open.read()
        print(text, end="")
