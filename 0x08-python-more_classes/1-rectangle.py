#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle:
    """Represent a rectangle"""


def __init__(self, width, height=0):
    """initialize  new rectangle.

    Args:
    width(int): the width of the new rectangle
    height(int): the height of the new rectangle
    """
    self.width = width
    self.height = height

    @property
    def width(self):
        """get/set the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, valu):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

        @property
        def height(self):
            """get/set the height of the rectangle."""
            return self._height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
