#!/usr/bin/python3
import json

"""to_json_string Module"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    json_obj = json.dumps(my_obj)
    return json_obj
