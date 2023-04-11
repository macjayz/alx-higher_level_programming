#!/usr/bin/python3
""" This describes inheritance """


class MyList(list):
    """ this prints lists """
    def print_sorted(self):
        print(sorted(self))
