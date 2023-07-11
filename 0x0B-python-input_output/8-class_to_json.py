#!/usr/bin/python3
"""Load items from a JSON file, extend command line arguments, and save back the file."""

import sys

if __name__ == "__main__":

    # Load save_to_json_file and load_from_json_file functions
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    # Try to load existing items from JSON file
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If file doesn't exist, initialize empty list
        items = []

    # Extend items list with command line arguments
    items.extend(sys.argv[1:])

    # Save updated items list back to JSON file
    save_to_json_file(items, "add_item.json")
