#!/usr/bin/python3
"""
0-read_file.py
A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads the contents of the file specified by filename.

    Prints the contents of the file to standard output
    without adding newlines after each line.

    The file is opened and read as UTF-8 encoded text.
    """

    with open(filename, encoding='UTF-8') as f:
        for line in f:
            print(line, end='')
