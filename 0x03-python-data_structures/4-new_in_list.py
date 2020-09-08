#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_copy = my_list.copy()
    if my_list_copy is None:
        return
    if -1 < idx < len(my_list_copy):
        my_list_copy[idx] = element
    return my_list_copy
