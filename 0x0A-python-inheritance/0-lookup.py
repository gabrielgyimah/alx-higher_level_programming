#!/usr/bin/python3

"""LooK Up Module"""


def lookup(obj):
    """
    Returns a list of all methods and attribute of an object.
    Args:
        obj(Object) : object whom method and attribute is to be return
    Raise:
        None
    Return:
        List of attributes and methods
    """
    return dir(obj)
