#!/usr/bin/python3
"""Module that defines a Square class that inherits from Rectangle."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle.

    Attributes:
        __size: The size of the square (private).
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            The area of the square (size * size).
        """
        return self.__size * self.__size
