#!/usr/bin/python3
"""
0-add_integer module.
 
This module defines a function that adds
two integers or floats together."""
 
 
def add_integer(a, b=98):
    """ Adds a and b together.
 
    Returns the resulting integer."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
