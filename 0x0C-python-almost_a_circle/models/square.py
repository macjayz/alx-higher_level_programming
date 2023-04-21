#!/usr/bin/python3
""" This module contains a super class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This a child class of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ intializing a constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size
        args:
            Value: returns int
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ This function updates objects using
        variable length arguments
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def __str__(self):
        """
        This will Overload str function
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """ This will return a dictionary representation of objects """
        obj_dictionary = {'id': self.id, 'size': self.size, 'x': self.x,
                          'y': self.y}

        return obj_dictionary
