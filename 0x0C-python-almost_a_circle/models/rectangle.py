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
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("heigth must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This returns the area """
        return (self.__width * self.__height)

    def display(self):
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ defines a varaible number of argument

        *args: this argument is used to pass multiple variables
       	1st argument should be the id attribute
	2nd argument should be the width attribute
	3rd argument should be the height attribute
	4th argument should be the x attribute
	5th argument should be the y attribute

        **kwargs: assigns a key/value or keyword argument to attributes
        """
        if args and len(args) != 0:
            itr = 0
            for arg in args:
                if itr == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif itr == 1:
                    self.width = arg
                elif itr == 2:
                    self.height = arg
                elif itr == 3:
                    self.x = arg
                elif itr == 4:
                    self.y = arg
                itr += 1

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    if b is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = b
                elif a == "width":
                    self.width = b
                elif a == "height":
                    self.height = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b
