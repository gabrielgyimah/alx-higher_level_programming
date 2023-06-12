#!/usr/bin/python3

"""Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates instances of the square class"""

    def __init__(self, size):
        """Initialize instances of the square class"""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """returns area of the Square."""
        return self.__size * self.__size

    def __str__(self) -> str:
        """Return the string representation of a Square instance"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
