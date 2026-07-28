#!/usr/bin/python3
"""Defines a function checking inheritance-inclusive class matching."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if obj is an instance of a_class, or an instance of any
        class that inherits (directly or indirectly) from a_class;
        False otherwise.
    """
    return isinstance(obj, a_class)
