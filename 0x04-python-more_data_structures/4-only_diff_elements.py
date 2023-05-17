#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    union_set = set_1.union(set_2)
    inter_set = set(set_1.intersection(set_2))
    new_set_list = union_set - inter_set

    if not set_1 or not set_2:
        return {}
    else:
        return set(new_set_list)
