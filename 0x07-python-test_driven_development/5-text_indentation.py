#!/usr/bin/python3
"""
module contains a function that prints a text with two new lines after
each character in `.?:`
"""


def text_indentation(text):
    """
   function prints a string in a specified format
    Args:
        text: the string to be printed
    Return:
        Has no return value
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    string = ""
    j = 0
    length = len(text)
    while j < length:
        if j == 0:  # ensure it doesn't begin with white space
            try:
                while text[j] == ' ':
                    j += 1
            except Exception:
                break
        string += text[j]

        if text[j] == '.' or text[j] == '?' or text[j] == ':':
            string += "\n\n"
            j += 1
            try:
                while text[j] == ' ':
                    j += 1
            except Exception:
                break
        else:
            j += 1

    j = 0
    length = len(string) - 1
    # trim white spaces at end
    if length != -1:
        while string[length] == " ":
            length -= 1
            j += 1
    if j != 0:
        string = string[:-j]
    print(string, end="")
