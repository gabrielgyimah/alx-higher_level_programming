#!/usr/bin/python3

"""append_write Module"""


def append_write(filename="", text=""):

    """
    appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """
    with open(file=filename, mode="w", encoding="UTF-8") as file:
        file.write(text)
        return file.seek(0, 2)
