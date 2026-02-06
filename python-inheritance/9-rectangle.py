#!/usr/bin/python3
"""Module that defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry.

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

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description.

        Returns:
            String in format: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
