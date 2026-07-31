#!/usr/bin/python3
"""Module that defines a function to check for an exact class match."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if type(obj) is exactly a_class, False otherwise
        (this excludes subclasses, unlike isinstance()).
    """
    return type(obj) is a_class
