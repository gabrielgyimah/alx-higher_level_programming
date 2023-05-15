#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        counter = 0
        new_list = []
        
        while counter < len(my_list):
            if counter == idx:
                pass
            else:
                new_list.append(my_list[counter])
            counter += 1

        return new_list


