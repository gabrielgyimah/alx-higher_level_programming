#!/usr/bin/python3


"""defines a square by: (based on 2-square.py)"""


class Square:
    """defines a square by: (based on 2-square.py)"""

    def __init__(self, size=0) -> None:
        """Initializes instances of the Square class"""
        if not isinstance(size, int):
                raise TypeError("size must be an integer")
        if size < 0:
             raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
         """Computes the area of the current Square object"""
         return self.__size ** 2
