#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @property
    def width(self):
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
        
    def area(self):
        """Return the area of the Rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2*self.__width)+(2*self.__height))
    
    def __str__(self):
        stri = ""
        for i in range(self.__height):
            for j in range(self.__width):
                stri += "#"
            stri+="\n"
        return stri
