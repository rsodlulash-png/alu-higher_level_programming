#!/usr/bin/python3
"""Defines a function checking indirect/direct class inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherited from a_class.

    Unlike is_kind_of_class(), this excludes the case where
    type(obj) is exactly a_class - obj's class must be a genuine
    subclass (direct or indirect) of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if obj is an instance of a class that inherits,
        directly or indirectly, from a_class; False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
