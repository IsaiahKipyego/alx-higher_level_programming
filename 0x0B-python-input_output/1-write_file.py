#!/usr/bin/python3
"""
A module containing a function writing a given file
"""


def write_file(filename="", text=""):
    """
    write_file:
        writes into given file, creates new file if it doesn't exits,
        overwrites old file if it exists
    Args:
        filename: name of the file
        text: text to be written
    """
    num_chars = 0
    with open(filename, "w", encoding="utf-8") as file_open:
        num_chars = file_open.write(text)
    return num_chars
