#!/usr/bin/python3


"""defines a square by: (based on 3-square.py)"""


class Square:
    """defines a square by: (based on 3-square.py)"""

    def __init__(self, size=0) -> None:
        """Initializes instance of the square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Returns the value of size for the current instance"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the current object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the current instance"""
        return self.__size ** 2
