#!/usr/bin/python3
"""Define an inherited class-checking class"""


def inherits_from(obj, a_class):
    """ checks if an object is an inheritd instances of a class.


    Args:
        obj(any): The object to checks
        a_class(type): the class to match the type of obj to
    Returns:
        if ob is an inherited instance of a_class - True
        otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
