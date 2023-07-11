#!/usr/bin/python3
"""Reads data from a JSON file and returns a Python object."""

import json

def load_from_json_file(filename):
    """Parse a JSON file and return a Python object."""
    with open(filename) as f:
        return json.load(f)
