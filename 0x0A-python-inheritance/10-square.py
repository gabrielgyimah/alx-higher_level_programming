#!/usr/bin/python3

"""Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates Square object."""

    def __init__(self, size):
        """Initialize instances of the square class"""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """returns the area of the Square."""
        return self.__size * self.__size
