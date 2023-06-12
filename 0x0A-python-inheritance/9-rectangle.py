#!/usr/bin/python3

"""Rectangle - Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates Rectangle object that inherits from BaseGeometry"""

    def __init__(self, width, height):

        """Initialize instance"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of the rectangle."""

        return self.__width * self.__height

    def __str__(self) -> str:
        """string reprsentation of rectangle."""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
