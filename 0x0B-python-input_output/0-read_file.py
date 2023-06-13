#!/usr/bin/python3

"""read_file Module"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""

    with open(filename, "r", encoding="UTF-8") as file:
        file_content = file.read()
        print(file_content)
