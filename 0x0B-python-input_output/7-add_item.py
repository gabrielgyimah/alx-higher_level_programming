#!/usr/bin/ptyhon3

"""Adds all command line args to a list"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    1. Adds all command line args to a list
    2. Save them to a file
    3. The list must be saved as a JSON representation
    4. file must be named add_item.json
    5. If the file doesn’t exist, it should be created
    6. Don’t need to manage file permissions / exceptions.
    """

    my_list = []

    try:
        my_list = load_from_json_file("add_item.json")
    except Exception:
        save_to_json_file(my_list, "add_item.json")

    if len(sys.argv) < 2:
        return

    for item in sys.argv:
        if item is sys.argv[0]:
            continue
        my_list.append(item)

    save_to_json_file(my_list, "add_item.json")


add_item()
