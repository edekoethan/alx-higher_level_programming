#!/usr/bin/python3
"""
if the object is an instance of retyrn true, or if the object is an instance of a class that inherited from the specified class return false
"""


def is_kind_of_class(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    return isinstance(obj, a_class)
