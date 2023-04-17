#!/usr/bin/python3
""" This is a child class of base class """
from models.base import Base


class Rectangle(Base):
    """ This is a child class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """A constructor has been initialized"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        pass

    @height.setter
    def height(self, value):
        pass

    @x.setter
    def x(self, value):
        pass

    @y.setter
    def y(self, value):
        pass
