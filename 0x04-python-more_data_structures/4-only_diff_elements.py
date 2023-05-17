#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    emp_set = {}
    union_set = set_1.union(set_2)
    inter_set = set_1.intersection(set_2)
    new_set = union_set - inter_set

    if not set_1 or not set_2:
        return emp_set
    else:
        return new_set
