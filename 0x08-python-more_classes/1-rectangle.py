#!/usr/bin/python3


"""Defines a Rectangle class."""


class Rectangle:
<<<<<<< HEAD
    def __init__(self, width=0, height=0):
=======
    def __init__(self, width = 0, height = 0):
        """ Initializes a new Rectangle.
        
        Args:
        width(int): the width of the new retangle.
        height(int): the height of the new rectnagle.
        """
>>>>>>> 2c35b185253dbd66023b2d43f5711b25d1f70660
        self.width = width
        self.height = height
    @property

    def width(self):
        """ Get/set width of the Rectangle."""
        
        return self.__width
    @width.setter

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError ("width must be an integer")
        if value < 0:
            raise ValueError ("width must be >= 0")
        self.__width = value
    @property

    def height(self):
        """ Get/set Height of the rectanle."""
        
        return self.__height
    @height.setter

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError (" height must be an integer")
        if value < 0:
            raise ValueError ("height must be >= 0")
        self.__height = value
