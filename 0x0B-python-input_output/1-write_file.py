#!/usr/bin/python3
""" Module that writes text to a file
"""


def write_file(filename="", text=""):
    """Function writes text to a file
    Args:
        filename: name of file
        text: text content to write
    Raises:
        Exception: if file can't be opened
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
