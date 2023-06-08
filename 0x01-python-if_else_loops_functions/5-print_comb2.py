#!/usr/bin/python3
for new_ number in range(0, 100):
    if new_number == 99:
        print("{}".format(new_number))
    else:
        print("{:02}".format(new_number), end=", ")
