#!/usr/bin/python3

"""Computes the the sum of two number"""


def add_integer(a, b=98):
    """
    computes the sum of two numbers

    Args:
        a(int/float): first number
        b(int/float): second number
    Raise:
        TypeError: if a or b is not int or float
    Return:
        (int): sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
