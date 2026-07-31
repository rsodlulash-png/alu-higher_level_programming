#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


class MyList(list):
    """A list subclass with an extra method to print itself sorted."""

    def print_sorted(self):
        """Print the list, sorted in ascending order."""
        print(sorted(self))
