#!/usr/bin/python3
""" Defines an integer addition function """


def add_integer(a, b=98):
    """return the integer addition of a and b.
    float argument are typecast to int before addition are performed.

    Raises:
    TypeError: if either of a or b  is a non-integer and non-float
    """
    if ((not type(a, int) and not type(a, float))):
        raise TypeError("a must be an integer")
    if ((not type(b, int) and not type(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
