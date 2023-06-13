#!/usr/bin/python3

"""A CLsss for creating students"""


class Student:
    """
    1. A CLsss for creating students
    2. Public instance attributes
        first_name
        last_name
        age
    3. Instantiation with first_name, last_name and age:
        def __init__(self, first_name, last_name, age):
    4. Public method def to_json(self): that retrieves a
        dictionary representation of a Student instance
        (same as 8-class_to_json.py)
        - If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved
    5. Not allowed to import any module
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name

        if not isinstance(age, int):
            raise TypeError("Age must be an a number")
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(it) is str for it in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}

        return self.__dict__
