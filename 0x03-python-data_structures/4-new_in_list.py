#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_my_list = my_list.copy()
    if -1 < idx < len(copy_my_list):
        copy_my_list[idx] = element
        return copy_my_list
