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
    5. Not allowed to import any module
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name

        if not isinstance(age, int):
            raise TypeError("Age must be an a number")
        self.age = age

    def to_json(self):
        return self.__dict__
