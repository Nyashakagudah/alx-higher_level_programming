#!/usr/bin/python3
"""
2-my_list.py
a class MyList that inherits from list
"""


class MyList(list):
    """ Public instance method: def print_sorted(self):
    that prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        """Prints the list in sorted ascending order."""
        print(sorted(self))
