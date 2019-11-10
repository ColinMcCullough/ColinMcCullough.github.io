from fractionclass import Fraction
import unittest 

class TestStringMethods(unittest.TestCase): 
    """Unit tests for Fractions Class
    Arguments:
        unittest {unittest}
    """
    def setUp(self):
        """Sets up Fraction properties to be tested""" 
        self.fr_one = Fraction(1,6)
        self.fr_two = Fraction(1,2)
        self.fr_three = Fraction(2,8)
        self.neg_fr = Fraction(-1,2)
        self.neg_den_fr = Fraction(1,-2)
    
    def test_properties(self):
        """Tests Fraction object properties""" 
        self.assertEqual(self.fr_one.num, 1) 
        self.assertEqual(self.fr_one.den, 6)

    def test_prop_with_neg_input(self):
        """Tests Fraction object properties with negative input""" 
        self.assertEqual(self.neg_fr.num, -1) 
        self.assertEqual(self.neg_fr.den, 2)
        self.assertEqual(self.neg_den_fr.num, -1) 
        self.assertEqual(self.neg_den_fr.den, 2)
    
    def test_bad_prop_type(self):
        """Tests Fraction object properties error raised from incorrect type as a parameter"""
        with self.assertRaises(TypeError):
            Fraction(1,"blue")
    
    def test_to_string(self):
        """Tests overrode __str__ Fraction object method output"""
        self.assertEqual(str(self.fr_one), '1/6')
        self.assertEqual(str(self.fr_two), '1/2')  
        self.assertEqual(str(self.neg_fr), '-1/2')
        self.assertEqual(str(self.neg_den_fr), '-1/2') 

    def test_add(self):
        """Tests overrode __add__ Fraction object method"""
        self.assertEqual(self.fr_two + self.fr_three, Fraction(3,4))
        self.assertEqual(self.neg_fr + self.neg_den_fr, Fraction(-1,1))
    
    def test_subtract(self):
        """Tests overrode __sub__ Fraction object method"""
        self.assertEqual(self.fr_two - self.fr_one, Fraction(1,3))
        self.assertEqual(self.neg_fr - self.neg_den_fr, Fraction(0,1))

    def test_multiply(self):
        """Tests overrode __mul__ Fraction object method"""
        self.assertEqual(self.fr_two * self.fr_one, Fraction(1,12))
        self.assertEqual(self.neg_fr * self.neg_den_fr, Fraction(1,4))
    
    def test_truediv(self):
        """Tests overrode __truediv__ Fraction object method"""
        self.assertEqual(self.fr_two / self.fr_one, Fraction(3,1))
        self.assertEqual(self.neg_fr / self.neg_den_fr, Fraction(1,1))

    def test_gcd(self):
        """Tests gcd method from Fraction class"""
        # case: a = b
        self.assertEqual(self.fr_one.gcd(13,13),13)
        # case: first num prime  
        self.assertEqual(self.fr_one.gcd(37,600),1) 
        # case: num is mult of den
        self.assertEqual(self.fr_one.gcd(20,100),20)
        #standard
        self.assertEqual(self.fr_one.gcd(624129,2061517),18913)  
    
    def test_equal(self):
        """Tests overrode __eq__ Fraction object method"""
        #test true
        self.assertEqual(self.neg_fr == self.neg_den_fr,True)  
        #test false
        self.assertEqual(self.fr_two == self.fr_one,False)

    def test_greater_than(self):
        """Tests overrode __gt__ Fraction object method"""
        #test true
        self.assertGreater(self.fr_two,self.fr_one)  
        #test false
        self.assertEqual(self.neg_den_fr > self.neg_fr,False)

    def test_greater_than_or_equal(self):
        """Tests overrode __ge__ Fraction object method"""
        #test true
        self.assertGreaterEqual(self.fr_two, self.fr_one) 
        self.assertGreaterEqual(self.neg_den_fr, self.neg_fr) 
        #test false
        self.assertEqual(self.fr_one >= self.fr_two,False)  

    def test_less_than(self):
        """Tests overrode __lt__ Fraction object method"""
        #test true
        self.assertLess(self.fr_one, self.fr_two)
        #test false
        self.assertEqual(self.fr_two < self.fr_one,False)  
    
    def test_less_than_or_equal(self):
        """Tests overrode __le__ Fraction object method"""
        #test true
        self.assertLessEqual(self.fr_one,self.fr_two)  
        self.assertEqual(self.neg_den_fr,self.neg_fr) 
        #test false
        self.assertEqual(self.fr_two <= self.fr_one,False)

    def test_not_equal(self):
        """Tests overrode __ne__ Fraction object method"""
        #test true
        self.assertEqual(self.fr_one != self.fr_two,True)   
        #test false
        self.assertEqual(self.neg_den_fr != self.neg_fr,False)

    def test_radd(self):  
        """Tests overrode __radd__ Fraction object method"""
        #test add 0
        self.assertEqual(0 + self.fr_two,self.fr_two)
        #test add num
        self.assertEqual(1 + self.fr_two,Fraction(3,2))
        #test adding not integer
        with self.assertRaises(TypeError):
            1.1 + self.fr_two
    
    def test_iadd(self):  
        """Tests overrode __iadd__ Fraction object method"""
        x = self.fr_two
        x += 0
        y = self.fr_one
        y += 1
        #test add 0
        self.assertEqual(x,self.fr_two)
        #test add num
        self.assertEqual(y,Fraction(7,6))
        #test bad type
        with self.assertRaises(TypeError):
            self.fr_two += 1.1
        
    def test_repr(self):
        """Tests overrode __repr__ Fraction object method"""
        self.assertEqual(repr(self.fr_two),"<class 'fractionclass.Fraction'>State: 1/2")
        self.assertEqual(repr(self.fr_one),"<class 'fractionclass.Fraction'>State: 1/6")

if __name__ == '__main__':
    unittest.main()
