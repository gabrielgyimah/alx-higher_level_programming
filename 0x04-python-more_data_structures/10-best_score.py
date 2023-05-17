#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    ans = None

    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary.get(ans, float("-inf")):
            ans = key

    return ans
