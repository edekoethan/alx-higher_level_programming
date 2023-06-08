#!/usr/bin/python3
import random
my_number = random.randint(-10, 10)
if my_number > 0:
    print("{} is positive".format(my_number))
elif my_number == 0:
    print("{} is zero".format(my_number))
else:
    print("{} is negative".format(my_number))
