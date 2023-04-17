#!/usr/bin/python3
""" This module contains a super class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This a child class of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ intializing a constructor """
        super().__init__(size, size, x, y, id)
