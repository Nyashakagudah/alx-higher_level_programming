#!/usr/bin/python3
"""Defines a class MyInt that inverts equality operators."""


class MyInt(int):
    """Invert == and != operators."""

    def __eq__(self, value):
        """Override == to return True if values are not equal."""
        return self.real != value

    def __ne__(self, value):
        """Override != to return True if values are equal."""
        return self.real == value
