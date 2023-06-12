#!/usr/bin/python3

"""check if object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """check if object is an instance of a class that inherited"""

    return not type(obj) is a_class and issubclass(type(obj), a_class)
