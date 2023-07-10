#!/usr/bin/python3
"""
0-lookup.py
A function that retrns list of available attributes and methods of object
"""


def lookup(obj):
    """Returns a list of attributes and methods of the input object.

    Args:
        obj (any): The object to inspect.
    Returns:
        list: A list of strings containing the names of `obj`'s attributes.
    """
    return dir(obj)
