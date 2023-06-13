#!/usr/bin/python3

"""append_after Module"""


def append_after(filename="", search_string="", new_string=""):
    """
    1. inserts a line of text to a file, after each line
        containing a specific string
    2. must use the with statement
    3. don’t need to manage file permission or file doesn't
        exist exceptions.
    4.  not allowed to import any module
    """
    content = ""

    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            content += line
            if search_string in line:
                content += new_string

    with open(filename, "w", encoding="UTF-8") as file:
        file.write(content)
