#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""sh.py: The sh module. It contains a superclass Shape and 3 subclasses Circle, Rectangle and Square"""
from math import pi
 
class Shape:
    """The superclass Shape with a color"""
    def __init__(self, color = 'red'):
        """Initializer"""
        self.color = color
 
    def __str__(self):
        """Self description for print() and str()"""
        return 'Shape(color={})'.format(self.color)
 
    def __repr__(self):
        """Representative description for repr()"""
        return self.__str__()  # re-direct to __str__() (not recommended)
 
class Circle(Shape):
    """The Circle class: a subclass of Shape with a radius"""
    def __init__(self, radius = 1.0, color = 'red'):
        """Initializer"""
        super().__init__(color)  # Call superclass' initializer
        self.radius = radius
 
    def __str__(self):
        """Self description for print() and str()"""
        return 'Circle({}, radius={})'.format(super().__str__(), self.radius)
 
    def __repr__(self):
        """Representative description for repr()"""
        return self.__str__()  # re-direct to __str__() (not recommended)
 
    def get_area(self):
        return self.radius * self.radius * pi
 
class Rectangle(Shape):
    """The Rectangle class: a subclass of Shape wit a length and width"""
    def __init__(self, length = 1.0, width = 1.0, color = 'red'):
        """Initializer"""
        super().__init__(color)
        self.length = length
        self.width = width
 
    def __str__(self):
        """Self description for print() and str()"""
        return 'Rectangle({}, length={}, width={})'.format(super().__str__(), self.length, self.width)
 
    def __repr__(self):
        """Representative description for repr()"""
        return self.__str__()  # re-direct to __str__() (not recommended)
 
    def get_area(self):
        return self.length * self.width
 
class Square(Rectangle):
    """The Square class: a subclass of Rectangle having the same length and width"""
    def __init__(self, side = 1.0, color = 'red'):
        """Initializer"""
        super().__init__(side, side, color)
 
    def __str__(self):
        """Self description for print() and str()"""
        return 'Square({})'.format(super().__str__())
 
# For Testing
if __name__ == '__main__':
    s1 = Shape('orange')
    print(s1)                # Shape(color=orange)
    print(s1.color)          # orange
    print(str(s1))           # Shape(color=orange)
    print(repr(s1))          # Shape(color=orange)
 
    c1 = Circle(1.2, 'orange')
    print(c1)                # Circle(Shape(color=orange), radius=1.2)
    print(c1.get_area())     # 4.523893421169302
    print(c1.color)          # orange
    print(c1.radius)         # 1.2
    print(str(c1))           # Circle(Shape(color=orange), radius=1.2)
    print(repr(c1))          # Circle(Shape(color=orange), radius=1.2)
 
    r1 = Rectangle(1.2, 3.4, 'orange')
    print(r1)                # Rectangle(Shape(color=orange), length=1.2, width=3.4)
    print(r1.get_area())     # 4.08
    print(r1.color)          # orange
    print(r1.length)         # 1.2
    print(r1.width)          # 3.4
    print(str(r1))           # Rectangle(Shape(color=orange), length=1.2, width=3.4)
    print(repr(r1))          # Rectangle(Shape(color=orange), length=1.2, width=3.4)
 
    sq1 = Square(5.6, 'orange')
    print(sq1)               # Square(Rectangle(Shape(color=orange), length=5.6, width=5.6))
    print(sq1.get_area())    # 31.359999999999996
    print(sq1.color)         # orange
    print(sq1.length)        # 5.6
    print(sq1.width)         # 5.6
    print(str(sq1))          # Square(Rectangle(Shape(color=orange), length=5.6, width=5.6))
    print(repr(sq1))         # Square(Rectangle(Shape(color=orange), length=5.6, width=5.6))