#!/usr/bin/python3
"""Module that defines Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width: The width of the rectangle (private).
        __height: The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
