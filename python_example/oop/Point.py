#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
point.py: The point module, which defines the Point class
"""
 
class Point:    # In Python 2, use: class Point(object):
    """A Point instance models a 2D point with x and y coordinates"""
 
    def __init__(self, x = 0, y = 0):
        """Initializer, which creates the instance variables x and y with default of (0, 0)"""
        self.x = x
        self.y = y
 
    def __str__(self):
        """Return a descriptive string for this instance"""
        return '({}, {})'.format(self.x, self.y)
 
    def __repr__(self):
        """Return a command string to re-create this instance"""
        return 'Point(x={}, y={})'.format(self.x, self.y)
 
    def __add__(self, right):
        """Override the '+' operator: create and return a new instance"""
        p = Point(self.x + right.x, self.y + right.y)
        return p
 
    def __mul__(self, factor):
        """Override the '*' operator: modify and return this instance"""
        self.x *= factor
        self.y *= factor
        return self
 
# Test
if __name__ == '__main__':
    p1 = Point()
    print(p1)      # (0.00, 0.00)
    p1.x = 5
    p1.y = 6
    print(p1)      # (5.00, 6.00)
    p2 = Point(3, 4)
    print(p2)      # (3.00, 4.00)
    print(p1 + p2) # (8.00, 10.00) Same as p1.__add__(p2)
    print(p1)      # (5.00, 6.00) No change
    print(p2 * 3)  # (9.00, 12.00) Same as p1.__mul__(p2)
    print(p2)      # (9.00, 12.00) Changed