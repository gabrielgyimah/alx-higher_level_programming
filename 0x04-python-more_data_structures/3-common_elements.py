#!/usr/bin/python3

def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return set_1, set_2
    else:
        new_set_list = []

        for word_set_1 in set_1:
            for word_set_2 in set_2:
                if word_set_2 == word_set_1:
                    new_set_list.append(word_set_1)
                else:
                    pass
        return set(new_set_list)
