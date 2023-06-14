#!/usr/bin/python3

"""A function that adds a new attribute to an object"""

def add_attribute(object, name, value):
    """
    1. Raise a TypeError exception, with the message <can't
        add new attribute> if the object can’t have new
        attribute
    2. not allowed to use try/except
    3. not allowed to import any module
    """

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
