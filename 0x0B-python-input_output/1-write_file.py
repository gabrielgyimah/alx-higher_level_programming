#!/usr/bin/python3

"""write_file Module"""


def write_file(filename="", text=""):

    """writes a string to a text file and returns the num of characters"""
    with open(file=filename, mode="w", encoding="UTF-8") as file:
        file.write(text)
        return file.seek(0, 2)
