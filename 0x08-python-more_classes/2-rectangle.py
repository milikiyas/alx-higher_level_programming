#!/usr/bin/python3
""" Defines a Rectangle class."""


class Rectangle:
    """Defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle
          Args:
              width(int): The width of the new rectangle.
              height(int): The height of the new rectangle.
          """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(" height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the area of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
