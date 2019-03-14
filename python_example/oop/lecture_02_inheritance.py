#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

###############################################################################
# Name        : lecture_02_inheritance.py
# Author      : 
# Version     :
# Copyright   : Your copyright notice
# Description : Create class Circle, sub class Cylinder
###############################################################################

# Load entire math package, but only expose pi atribute
from math import pi

class Circle:
    """ Circle class - base class """
    def __init__(self, _radius = 1.0):
        """ Initializer with default radius of 1.0 """
        self.set_radius(_radius)

    # Invoke when call print() function
    def __str__(self):
        return "Circle with radius = {}".format(self._radius)

    def set_radius(self, _radius):
        if _radius <= 0:
            raise ValueError("Radius must be non-negative")
        else:
            self._radius = _radius

    def get_radius(self):
        return self._radius

    def get_area(self):
        return self._radius * self._radius * pi

# Sub class 'Cylinder' derive from base class 'Circle'
class Cylinder(Circle):
    """ Cylinder class - sub class """
    def __init__(self, _radius=1.0, _height=1.0):
        """ Initializer with default radius of 1.0, height of 1.0 """
        # Call base class construtor
        super().__init__(_radius)
        self.set_height(_height)
    
    # Override magic method of base class
    # if __str__ not define in subclass Cylinder
    # __str__ in base class Circle will be invoke        
    def __str__(self):
        return "Cylinder with radius = {}, height = {}".\
            format(self._radius, self._height)

    def set_height(self, _height):
        if _height <= 0:
            raise ValueError("Height must be non-negative")
        else:
            self._height = _height

    def get_height(self):
        return self._height

    def get_volume(self):
        return super().get_area() * self._height

if __name__ == '__main__':
    # Test base class - Circle
    c1 = Circle()  # Radius = 1.0 default
    print("---")
    print(c1)
    print("Radius of Circle = ", c1.get_radius())
    print("Area of Circle = ", c1.get_area())

    c2 = Circle(3)  
    print("---")
    print(c2)
    print("Radius of Circle = ", c2.get_radius())
    print("Area of Circle = ", c2.get_area())

    # Test sub class - Cylinder
    cy1 = Cylinder(2, 3)
    print("---")
    print(cy1)  # Invoke __str__ method in subclass Cylinder
    print("Radius of Cylinder = ", cy1.get_radius()) # call method in Cicle class
    print("Height of Cylinder = ", cy1.get_height()) # call method in Cylinder class
    print("Volume of Cylinder = ", cy1.get_volume()) # call method in Cylinder class
