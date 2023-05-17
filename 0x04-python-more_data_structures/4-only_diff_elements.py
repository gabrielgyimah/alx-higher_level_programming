#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = []

    if not set_1 or not set_2:
        return set(new_set)
    else:
        for word_1 in set_1:
            if word_1 not in set_2:
                new_set.append(word_1)
            else:
                pass
        for word_2 in set_2:
            if word_2 not in set_1 and word_2 not in new_set:
                new_set.append(word_2)
            else:
                pass
        return set(new_set)
