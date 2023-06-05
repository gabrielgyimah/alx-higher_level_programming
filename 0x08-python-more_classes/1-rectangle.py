#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """Defines a Rectangle class"""

    def __init__(self, width=0, height=0):
        """Instantiates the class objects"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        self.__width = width
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Returns the width of the current object"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the current object"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the current object"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the current object"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
