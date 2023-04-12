#!/usr/bin/python3
""" This function gets file input """


def read_file(filename=""):
    """ This function prints file to stdout """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
