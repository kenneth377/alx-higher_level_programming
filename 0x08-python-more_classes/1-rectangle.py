#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height
    
    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width
    
    
    @height.setter
    def height(self,value):
        if isinstance(value,int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("heigth must be >= 0")
        else:
            raise TypeError("heigth must be an integer")

    @width.setter
    def width(self,value):
        if isinstance(value,int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
