#!/usr/bin/python3
# 6-from_json_string.py
"""Converts a JSON string to a Python object."""

import json

def from_json_string(json_string):
   """Parse a JSON string and return the equivalent Python object."""
   return json.loads(json_string)
