#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    key_found = 0

    for dic_key in a_dictionary:
        if dic_key == key:
            key_found = 1
        else:
            pass

    if key_found == 1:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
        
    return a_dictionary
