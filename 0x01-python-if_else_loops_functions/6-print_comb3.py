#!/usr/bin/python3
for number in range(0, 100):
    first = number / 10
    last = number % 10
    if first < last and number != 89:
        print("{:02}, ".format(number), end="")
    elif number == 89:
        print("{}".format(number))
