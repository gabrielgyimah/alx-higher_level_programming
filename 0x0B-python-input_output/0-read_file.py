#!/usr/bin/python3

"""read_file Module"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""

    with open(file=filename, mode="r", encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
