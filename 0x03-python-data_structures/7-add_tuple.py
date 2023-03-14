#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a or tuple_b have less than 2 elements, add a 0 to the end
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Take only the first 2 elements of the tuples
    a, b = tuple_a[:2]
    c, d = tuple_b[:2]

    # Add the elements together and return the resulting tuple
    return (a+c, b+d)
