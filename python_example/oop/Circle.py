#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
1. Information for current modules
"""
from math import pi
 
class Circle:    # For Python 2 use: "class Circle(object):"
    """2. Infomation for class"""
 
    def __init__(self, radius=1.0):
        """Initializer with default radius of 1.0"""
        self.radius = radius  # Create an instance variable radius
 
    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return 'This is a circle with radius of {:.2f}'.format(self.radius)
 
    def __repr__(self):
        """Return a formal string that can be used to re-create this instance, invoked by repr()"""
        return 'Circle(radius={})'.format(self.radius)
 
    def get_area(self):
        """3. Info for this method"""
        return self.radius * self.radius * pi
 
# For Testing under Python interpreter
# If this module is run under Python interpreter, __name__ is '__main__'.
# If this module is imported into another module, __name__ is 'circle' (the module name).
if __name__ == '__main__':
    c1 = Circle(2.1)      # Construct an instance
    print(c1)             # Invoke __str__(): This is a circle with radius of 2.10
    print(c1.get_area())  # 13.854423602330987
    print(c1.radius)      # 2.1
    print(str(c1))        # Invoke __str__(): This is a circle with radius of 2.10
    print(repr(c1))       # Invoke __repr__(): Circle(radius=2.1)

    c2 = Circle()         # Default radius
    print(c2)
    print(c2.get_area())  # Invoke member method
 
    c2.color = 'red'  # Create a new attribute for this instance via assignment
    print(c2.color)
    #print(c1.color)  # Error - c1 has no attribute color
 
    # Test doc-strings
    print(__doc__)                  # This module
    print(Circle.__doc__)           # Circle class
    print(Circle.get_area.__doc__)  # get_area() method
 
    print(isinstance(c1, Circle)) # True
    print(isinstance(c2, Circle)) # True
    print(isinstance(c1, str))    # False