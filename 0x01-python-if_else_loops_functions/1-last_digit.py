#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absnumber = abs(number)
lastdigit = absnumber % 10

if number < 0:
    lastdigit = lastdigit * -1
if lastdigit > 5:
    print("last digit of {} is {} and is greater than 5"
          .format(number, lastdigit))
elif lastdigit == 0:
    print("last digit of {} is {} and is 0"
          .format(number, lastdigit))
else:
    print("last digit of {} is {} and is less than 6 and not 0"
          .format(number, lastdigit))
