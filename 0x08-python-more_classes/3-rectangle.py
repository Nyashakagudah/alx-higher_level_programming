#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """ Defines a rectangle. """

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle.
        Args:
            width (int): Width of the rectangle. Default is 0.
            height (int): Height of the rectangle. Default is 0.
        """

        self.width = width
        self.height = height

    # Width and height properties...

        def area(self):
            """Calculates the area of the rectangle.
            Returns:
                int: The area.
            """
            return self.width * self.height

        # Perimeter method...

    my_rectangle = Rectangle(10, 20)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
