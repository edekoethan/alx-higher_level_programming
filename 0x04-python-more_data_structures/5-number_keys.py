#!/usr/bin/python3
def number_keys(a_dictionary):
    number_of_keys = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        number_of_keys = number_of_keys + 1

    return (number_of_keys)
