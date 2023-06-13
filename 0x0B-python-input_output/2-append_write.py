#!/usr/bin/python3

"""append_write Module"""


def append_write(filename="", text=""):

    """
    appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """
    len_of_file = 0

    with open(file=filename, mode="a", encoding="UTF-8") as file:
        len_of_file = file.write(text)

    return len_of_file
