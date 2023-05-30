#!/usr/bin/python3


"""creates a new template of type square"""


class Square:
    """creates a new instance of type  Square."""

    def __init__(self, size=0):
        """Initializes instances of the Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Returns the value of the instances size field"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the value o the instances field size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a square"""
        return self.__size ** 2

    def __eq__(self, other) -> bool:
        """Check if two instances have equal area's"""
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        """Check if two object are not equal."""
        return self.area() != other.area()

    def __lt__(self, other) -> bool:
        """Checks if self's area is less than other's area"""
        return self.area() < other.area()

    def __gt__(self, other) -> bool:
        """Cheks if one instance's area is greter than the other"""
        return self.area() > other.area()

    def __le__(self, other) -> bool:
        """Check if one object is less than or equal to the other."""
        return self.area() <= other.area()

    def __ge__(self, other) -> bool:
        """Check if one object is greater than or equal to the other."""
        return self.area() >= other.area()
