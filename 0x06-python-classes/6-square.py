#!/usr/bin/python3


"""creates a new template of type  Square."""


class Square:
    """creates a new template of type  Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the instances o the class square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if len(position) != 2 or not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns the value of size of the current instance"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the field size value o the current instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Get the field position value."""
        return self.__position

    @position.setter
    def position(self, position):
        """Set the field position value."""
        if len(position) != 2 or not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def area(self):
        """Compute the area of a square."""
        return self.__size ** 2

    def my_print(self):
        """Print the a physical representation of the square."""
        if not self.size:
            print()
            return
        print('\n' * self.__position[1], end='')
        for i in range(self.size):
            s = '#' * self.size
            print(' ' * self.__position[0], end='')
            print(s)
