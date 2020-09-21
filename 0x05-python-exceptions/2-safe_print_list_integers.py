#!/usr/bin/python3
# prints the first x elements of a list and only integers
def safe_print_list_integers(my_list=[], x=0):
    real_number = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            real_number += 1
        except (TypeError, ValueError):
            pass
    print()
    return real_number
