#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods of an object.
"""


def lookup(obj):
    """This function looks out for all  attribute and methods of an object."""
    return dir(obj)
