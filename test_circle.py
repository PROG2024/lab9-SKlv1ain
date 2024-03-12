"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import sys
from math import hypot

# TODO write 3 tests as described above

class CircleTest(unittest.TestCase):
    
    
    def setUp(self) -> None:
        ...
        
        
    def test_typical_add_area(self):
        c1 = Circle(1)
        r1 = c1.get_radius()
        self.assertEqual(1, r1)
        
        c2 = Circle(2)
        r2 = c2.get_radius()
        self.assertEqual(2, r2)
        
        c3 = c2.add_area(c1)
        r3 = c3.get_radius()
        self.assertEqual(hypot(r1,r2), r3)
        
        
    def test_one_circle_radius_0(self):
        c1 = Circle(0)
        r1 = c1.get_radius()
        self.assertEqual(0, r1)
        
        c2 = Circle(2)
        r2 = c2.get_radius()
        self.assertEqual(2, r2)
        
        c3 = c2.add_area(c1)
        r3 = c3.get_radius()
        self.assertEqual(hypot(r1,r2), r3)
        
        
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
            

        
        
        
    
    
    