#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""cylinder.py: The cylinder module, which defines the Cylinder class"""
from circle import Circle  # Using the Circle class in the circle module
 
class Cylinder(Circle):
    """The Cylinder class is a subclass of Circle"""
 
    def __init__(self, radius = 1.0, height = 1.0):
        """Initializer"""
        super().__init__(radius)  # Invoke superclass' initializer (Python 3)
            # OR
            # super(Cylinder, self).__init__(radius)   (Python 2)
            # Circle.__init__(self, radius)            Explicit superclass class
        self.height = height
 
    def __str__(self):
        """Self Description for print() and str()"""
        # If __str__ is missing in the subclass, print() will invoke the superclass version!
        return 'Cylinder(radius={},height={})'.format(self.radius, self.height)

    def __repr__(self):
        """Formal Description for repr()"""
        # If __repr__ is missing in the subclass, repr() will invoke the superclass version!
        return self.__str__()   # re-direct to __str__() (not recommended)
 
    def get_volume(self):
        """Return the volume of the cylinder"""
        return self.get_area() * self.height  # Inherited get_area()
 
# For testing
if __name__ == '__main__':
    cy1 = Cylinder(1.1, 2.2)  # Output: Cylinder(radius=1.10,height=2.20)
    print(cy1)                # Invoke __str__()
    print(cy1.get_area())     # Use inherited superclass' method
    print(cy1.get_volume())   # Invoke its method
    print(cy1.radius)
    print(cy1.height)
    print(str(cy1))           # Invoke __str__()
    print(repr(cy1))          # Invoke __repr__()
 
    cy2 = Cylinder()          # Default radius and height
    print(cy2)                # Output: Cylinder(radius=1.00,height=1.00)
    print(cy2.get_area())
    print(cy2.get_volume())
 
    print(dir(cy1))
        # ['get_area', 'get_volume', 'height', 'radius', ...]
    print(Cylinder.get_area)
        # <function Circle.get_area at 0x7f490436b378>
        # Inherited from the superclass
    print(Circle.get_area)
        # <function Circle.get_area at 0x7f490436b378>
 
    print(issubclass(Cylinder, Circle))  # True
    print(issubclass(Circle, Cylinder))  # False
    print(isinstance(cy1, Cylinder))     # True
    print(isinstance(cy1, Circle))       # True (A subclass object is also a superclass object)
    print(Cylinder.__base__)             # Show superclass: <class 'circle.Circle'>
    print(Circle.__subclasses__())       # Show a list of subclasses: [<class '__main__.Cylinder'>]
 
    c1 = Circle(3.3)
    print(c1)                        # Output: This is a circle with radius of 3.30
    print(isinstance(c1, Circle))    # True
    print(isinstance(c1, Cylinder))  # False (A superclass object is NOT a subclass object)