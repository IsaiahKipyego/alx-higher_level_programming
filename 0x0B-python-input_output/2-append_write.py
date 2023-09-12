#!/usr/bin/python3
"""
module with a function that appends text to a file
"""


def append_write(filename="", text=""):
    """
    A function appending text to a file and creates new file if doesn't exist
    Args:
        filename: name of the file
        text: text to append
    """
    num_chars = 0
    with open(filename, "a", encoding="utf-8") as file_open:
        num_chars = file_open.write(text)
    return num_chars
