#!/usr/bin/python3

from models.base import Base
"""Class Rectangle
"""


class Rectangle(Base):
    """Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
