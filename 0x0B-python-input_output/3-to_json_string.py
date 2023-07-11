#!/usr/bin/python3
"""Defines a string-to-JSON function."""

import json

# Function to convert a Python object to JSON string
def to_json_string(my_obj):
    """Return the JSON representation of a string object."""

    # Convert object to JSON string using json.dumps
    return json.dumps(my_obj)

# Example usage:
my_dict = {"name": "John", "age": 30}
json_str = to_json_string(my_dict)
print(json_str)
