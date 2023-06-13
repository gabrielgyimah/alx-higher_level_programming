#!/usr/bin/python3

"""class_to_json Module."""


def class_to_json(obj):
    """
    1. obj is an instance of a Class
    2. All attributes of the obj Class are serializable: list,
    dictionary, string, integer and boolean
    3. not allowed to import any module
    """
    return obj.__dict__
