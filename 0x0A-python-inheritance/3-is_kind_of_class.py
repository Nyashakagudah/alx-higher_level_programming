#!/usr/bin/python3
"""
===================================
Module with the method is_kind_of_class
===================================
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or subclass.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass.
             False otherwise.
    """
    return isinstance(obj, a_class)
