#!/usr/bin/python3
"""Defines a lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return dir(obj)
