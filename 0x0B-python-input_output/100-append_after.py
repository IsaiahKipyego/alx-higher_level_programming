#!/usr/bin/python3
"""
A module inserting a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Searches specific str and adds a line of text to file if string
    is present
    Args:
        filename: the name of file
        search_string: string to search
        new_string: string to insert
    """
    text = ""
    # open and search file
    with open(filename, encoding="utf-8") as file_open:
        for line in file_open:
            text += line
            if search_string in line:
                text += new_string

    # open and write into the file
    with open(filename, "w", encoding="utf-8") as file_write:
        file_write.write(text)
