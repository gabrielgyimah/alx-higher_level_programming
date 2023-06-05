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

    def area(self):
        """Returns the area of the current rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the permiter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        perim = 2 * (self.__height + self.__width)
        return perim

    def __str__(self):
        """Returns the string rep in the for #"""
        if self.__height == 0 or self.__width == 0:
            return ""

        i = 0
        ret_str = ""
        while(i < self.__height):
            ret_str += "#" * self.__width
            ret_str += "\n"
            i += 1
        return ret_str[:len(ret_str) - 1]

    def print(self) -> str:
        """Returns the offical string representation of the object"""
        if self.__height == 0 or self.__width == 0:
            return ""

        i = 0
        ret_str = ""
        while i < self.__height:
            ret_str = "#" * self.__width
            print(ret_str)
            i += 1

    @classmethod
    def eval(cls, instance):
        """converter"""
        width, height = instance.split()
        width = width[10:]
        width = int(width[:len(width) - 1])
        height = int(height[:len(height) - 1])

        return cls(width, height)

    def __repr__(self) -> str:
        """"Returns a string representation of the object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
