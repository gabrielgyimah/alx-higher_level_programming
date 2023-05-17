#!/usr/bin/python3

def number_keys(a_dictionary):
    if not a_dictionary:
        return 0
    else:
        counter = 0
        for key in a_dictionary:
            counter += 1
        return counter
