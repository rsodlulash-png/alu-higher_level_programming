#!/usr/bin/python3
"""Defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Base class intended for future geometry subclasses."""

    def area(self):
        """Raise an Exception - subclasses must override this method."""
        raise Exception("area() is not implemented")
