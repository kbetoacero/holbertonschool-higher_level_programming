#!/usr/bin/python3
def no_c(my_string):
    my_string2 = list(my_string)
    for i in range(my_string2.count('c')):
        my_string2.remove('c')
    for i in range(my_string2.count('C')):
        my_string2.remove('C')
    str2 = ""
    return str2.join(my_string2)
