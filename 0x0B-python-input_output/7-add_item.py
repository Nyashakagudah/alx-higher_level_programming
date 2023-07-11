#!/usr/bin/python3
"""Load items from a JSON file, add command line arguments to the items list, and save back to the file."""

import sys

if __name__ == "__main__":

    # Import functions to load/save JSON file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    # Try to load existing items from JSON file
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If file doesn't exist, initialize empty list
        items = []

    # Add command line arguments to list
    items.extend(sys.argv[1:])

    # Save updated list back to JSON file
    save_to_json_file(items, "add_item.json")
