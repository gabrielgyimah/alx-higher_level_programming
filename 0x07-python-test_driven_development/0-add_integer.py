#!/usr/bin/python3

"""add_integer Module"""


def add_integer(a, b=98):
    """
    1. a and b must be integers or floats, otherwise raise a
        TypeError exception with the message a must be an
        integer or b must be an integer
    2. a and b must be first casted to integers if they are float
    3. Returns an integer: the addition of a and b
    4. not allowed to import any module
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    ans = int(a) + int(b)
    return ans
