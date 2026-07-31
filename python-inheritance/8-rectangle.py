#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle, with private width and height."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle, must be > 0.
            height (int): the height of the rectangle, must be > 0.

        Raises:
            TypeError: if width or height is not an integer.
            ValueError: if width or height is <= 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
