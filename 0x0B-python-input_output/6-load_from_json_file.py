#!/usr/bin/python3

"""load_from_json_file Module"""
import json


def load_from_json_file(filename):
    """
    1. A function that creates an Object from a “JSON file”:
    2. use the with statement
    3. Don't need to manage exceptions if the JSON string
    doesn't represent an object.
    4. Don't need to manage file permissions / exceptions.
    """

    with open(filename, "r") as file:
        json_obj = json.load(file)
        return json_obj
