#!/usr/bin/python3

"""to_json_string Module"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    json_obj = json.dumps(my_obj)
    return json_obj
