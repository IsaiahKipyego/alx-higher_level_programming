#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    """Implements sorted printing for built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        l_a = sorted(self)
        print(l_a)
