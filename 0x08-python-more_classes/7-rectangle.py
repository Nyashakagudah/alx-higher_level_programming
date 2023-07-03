#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ Tracks number of instances and print symbol """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes width and height, increments instance count """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Gets width """

        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width, checks if int >= 0 """

        if not isinstance(value, int):
            raise TypeError("Must be int")
        if value < 0:
            raise ValueError("Must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets height """

        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height, checks if int >= 0 """

        if not isinstance(value, int):
            raise TypeError("Must be int")
        if value < 0:
            raise ValueError("Must be >= 0")
        self.__height = value
