from recursion import *
import unittest
import turtle
import random
from timeit import Timer
import time 

class TestStringMethods(unittest.TestCase): 
    """Unit tests for Fractions Class
    Arguments:
        unittest {unittest}
    """
    def setUp(self):
        self.t = turtle.Turtle()
    
    def test_get_factorial(self):
        """Tests Fraction object properties""" 
        with self.assertRaises(ValueError):
            get_factorial(-1)
        self.assertEqual(get_factorial(0),1)
        self.assertEqual(get_factorial(1),1)
        self.assertEqual(get_factorial(5),120)
    
    def test_reverse_lst(self):
        self.assertEqual(reverse_lst([]),[])
        self.assertEqual(reverse_lst([1]),[1])
        self.assertEqual(reverse_lst([1,2,3,4,5]),[5,4,3,2,1])
        self.assertEqual(reverse_lst(['a','b','c','d']),['d','c','b','a'])

    def test_fib(self):
        self.assertTrue(fib(1) == 1)
        self.assertTrue(fib(2) == 1)
        self.assertTrue(fib(5) == 5)
        self.assertTrue(fib(9) == 34)
    
    def test_non_recursive(self):
        self.assertTrue(fib_non_recurse(1) == 1)
        self.assertTrue(fib_non_recurse(2) == 1)
        self.assertTrue(fib_non_recurse(5) == 5)
        self.assertTrue(fib_non_recurse(9) == 34)

    def test_tree_setup(self):
        
        tree_setup(self.t)
        x,y = self.t.position()
        self.assertEqual(self.t.color()[0],'brown')
        self.assertEqual(y,-200.00)
        self.assertEqual(self.t.pensize(),10)

    def test_mod_tree_attr(self):
        degree,mod = mod_tree_attr(self.t,20,10)
        self.assertEqual(self.t.pensize(),20)
        self.assertIsInstance(degree,int)
        self.assertIsInstance(mod,int)
    
    def test_time_test_fib(self):
        self.assertIsInstance(time_test_fib(5),str)
        self.assertIsInstance(time_test_fib(1),str)

    def test_jug_juggling(self):
        self.assertTrue(jug_juggling(4,0,3,0,2))
        self.assertTrue(jug_juggling(8,0,6,0,4))

if __name__ == '__main__':
    unittest.main()