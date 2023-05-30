#!/usr/bin/python3


"""a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """a class Square that defines a square by: (based on 4-square.py)"""

    def __init__(self, size=0) -> None:
        """Initializes the class instances"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Returns the value of size of the current instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size of the current instance"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the current instance"""
        return self.__size ** 2

    def my_print(self):
        """prints the string representation of the instance"""
        if self.__size == 0:
            pass
        else:
            for i in range (self.size):
                s = '#' * self.size
                print(s)
        print()
