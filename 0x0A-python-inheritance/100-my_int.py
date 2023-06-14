#!/usr/bin/python3

"""a class MyInt that inherits from int"""


class MyInt(int):
    """
    1. MyInt is a rebel. MyInt has == and != operators inverted
    2. not allowed to import any module
    """

    def __init__(self, num) -> int:
        self.num = num

    def __str__(self) -> str:
        return str(self.num)

    def __eq__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
