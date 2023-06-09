#!/usr/bin/python3

"""Simple Rectangle Module."""


class Rectangle:
    """Represent a Rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the an object Rectangle type."""
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the value of width."""
        return self.__width

    @width.setter
    def width(self, val):
        """Set the value of width."""
        if not type(val) is int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """Get the value of height."""
        return self.__height

    @height.setter
    def height(self, val):
        """Set the value of height."""
        if not type(val) is int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """Returns the area of a Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a Rectangle."""
        if not self.__width or not self.__height:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def print(self):
        """Prints the string representation of a Rectangle"""
        if not self.__width or not self.__height:
            return
        i = 0
        while i < self.__height:
            s = str(self.print_symbol) * self.__width
            print(s)
            i += 1

    def __str__(self):
        """Return string representation of a Rectangle"""
        if not self.__width or not self.__height:
            return ""
        i = 0
        out = ""
        while i < self.__height:
            out += str(self.print_symbol) * self.__width
            out += "\n"
            i += 1
        return out[:len(out) - 1]

    def __repr__(self) -> str:
        """Returns string representation of an object"""
        return f"Rectangle({self.__width}, {self.__height})"

    @classmethod
    def eval(cls, obj):
        """Converter"""
        w, h = obj.split()
        w = w[10:]
        w = int(w[:len(w) - 1])
        h = int(h[:len(h) - 1])

        return cls(w, h)

    def __del__(self):
        """Alert that we have an object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
