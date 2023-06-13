#!/usr/bin/python3

"""save_to_json_file Module"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation:
    You must use the with statement
    You don't need to manage exceptions if the object
    can't be serialized.
    You don't need to manage file permission exceptions.
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
