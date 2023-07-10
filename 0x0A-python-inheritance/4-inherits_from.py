#!/usr/bin/python3
"""
==================================
Module with the method inherits_from
==================================
"""


def inherits_from(obj, a_class):
    """
    Method that checks if an object inherits from a class.

    Args:
        obj: The object to check.
        a_class: The class type to compare against.

    Returns:
        True if obj inherits from a_class.
        False otherwise.
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
