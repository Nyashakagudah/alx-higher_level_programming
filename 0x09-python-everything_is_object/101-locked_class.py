#!/usr/bin/python3
"""
Module for class prevents dynamic attributes creation
"""


class LockedClass():
    """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
