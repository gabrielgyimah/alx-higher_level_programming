#!/usr/bin/python3

"""function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>

    Args:
        first_name(string): first argument
        last_name(string): second argument

    Raise:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string

    Return:
        None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
