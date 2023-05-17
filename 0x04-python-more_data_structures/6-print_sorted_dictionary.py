#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_dic = sorted(a_dictionary.keys())

    for key in new_dic:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
