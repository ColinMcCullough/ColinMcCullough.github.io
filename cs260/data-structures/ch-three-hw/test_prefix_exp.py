from prefix_exp import *
import unittest 

class TestStringMethods(unittest.TestCase): 
    """Unit tests for prefix_exp file
    Arguments:
        unittest {unittest}
    """
    def test_tokenize(self):
        self.assertEqual(tokenize('1*(22+3)/5'), ['1', '*', '(', '22', '+', '3', ')', '/', '5'])
        self.assertEqual(tokenize('1  + 1'), ['1', '+', '1'])
        self.assertEqual(tokenize('1 ** 1'), ['1', '**', '1'])
        self.assertEqual(tokenize('1 // 1'), ['1', '//', '1'])
        self.assertEqual(tokenize('244+( 77 / 3) * 4'), ['244', '+', '(','77','/','3',')','*','4'])  
        self.assertEqual(tokenize(''), [])
    
    def test_checkbalance(self):
        self.assertEqual(checkbalance(['(','(',')',')','(','(',]),False)
        self.assertEqual(checkbalance(['(','(',')',')','(',')',]),True)
        self.assertEqual(checkbalance([]),True)
    
    def test_infixToPostfix(self):
        with self.assertRaises(Exception):
            infixToPostfix('1*(22+3))/5')
        self.assertEqual(infixToPostfix('1 * 5'),'1 5 *')
        self.assertEqual(infixToPostfix('(1 - 3) * (6*4)'),'1 3 - 6 4 * *')
        self.assertEqual(infixToPostfix('4 ** 2 + 5'),'4 2 ** 5 +')
        self.assertEqual(infixToPostfix('3 * 4 - 5 // 5'),'3 4 * 5 5 // -')  
        self.assertEqual(infixToPostfix('1*(22+3)/5'),'1 22 3 + * 5 /')
    
    def test_postfixEval(self):
        with self.assertRaises(Exception):
            postfixEval([1,2,3])
        self.assertEqual(postfixEval('1 5 *'),5)
        self.assertEqual(postfixEval('1 3 - 6 4 * *'),-48)
        self.assertEqual(postfixEval('1 22 3 + * 5 /'),5.0)
        self.assertEqual(postfixEval('3 ** 2'),9)
        self.assertEqual(postfixEval('3 // 2'),1)
    
    def test_doMath(self):
        with self.assertRaises(Exception):
            doMath(3,3,3)
        with self.assertRaises(Exception):
            doMath('*',3,'4')
        with self.assertRaises(Exception):
            doMath('*','3',4)
        with self.assertRaises(ArithmeticError):
            doMath('?',3,4)
        self.assertEqual(doMath('*',3,4),12)
        self.assertEqual(doMath('*',-3,4),-12)
        self.assertEqual(doMath('/',20,4),5)
        self.assertEqual(doMath('+',20,4),24)
        self.assertEqual(doMath('-',20,4),16)

if __name__ == '__main__':
    unittest.main()