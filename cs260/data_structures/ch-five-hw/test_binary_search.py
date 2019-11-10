import unittest
from binarysearch import *
import random

class TestStringMethods(unittest.TestCase): 
    """Unit tests for Binary Search Exercises
    Arguments:
        unittest {unittest}
    """
    def setUp(self):
        self.lst = [i for i in range(1000)]
    
    def test_time_decorator(self):
        @time_decorator
        def test(a,b):
            return a+b
        x,y = test(1,2)
        self.assertIsInstance(y,float)

    def test_time_decorator_2(self):
        @time_decorator_2
        def test1(a,b,c,d):
            return a+b+c
        x,y = test1(1,2,3,4)
        self.assertIsInstance(y,float)

    def test_binarySearch(self):
        self.assertEqual(binarySearch(self.lst, 100),True)
        self.assertEqual(binarySearch(self.lst, -100),False)

    def test_rec_bin_search(self):
        self.assertEqual(binarySearch(self.lst, 100),True)
        self.assertEqual(binarySearch(self.lst, -100),False)

    def test_recur_bin_srch_noslice(self):
        self.assertEqual(binarySearch(self.lst, 100),True)
        self.assertEqual(binarySearch(self.lst, -100),False)

if __name__ == '__main__':
    unittest.main()