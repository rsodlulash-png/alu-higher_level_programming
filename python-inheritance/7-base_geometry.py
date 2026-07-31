#!/usr/bin/python3
"""Defines a BaseGeometry class with area and integer validation."""


class BaseGeometry:
    """Base class intended for future geometry subclasses."""

    def area(self):
        """Raise an Exception - subclasses must override this method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): the name of the attribute being validated,
                used in the error message.
            value: the value to validate.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
