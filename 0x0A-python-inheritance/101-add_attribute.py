#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to. # The object
        att (str): The name of attribute to add obj. # The attrbute name
        value (any): The value of att. # The attribute value
    Raises:
        TypeError: If the attribute cannot be added.
    """
    # Check if the object is mutable
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    # Set the attribute
    setattr(obj, att, value)
