from parsetree import *
import unittest

class BinaryParseTreeTests(unittest.TestCase):

    def test_build_parse_tree(self):
        x = build_parse_tree('(1+1)')
        self.assertEqual(x.getRootVal(),'+')
        self.assertEqual(x.getLeftChild().key,1)
        self.assertEqual(x.getRightChild().key,1)
        y = build_parse_tree('((10*6) + (4/3))')
        self.assertEqual(y.getRootVal(),'+')
        self.assertEqual(y.getLeftChild().key,'*')
        self.assertEqual(y.getRightChild().key,'/')
        self.assertEqual(y.getLeftChild().getLeftChild().key,10)
        self.assertEqual(y.getLeftChild().getRightChild().key,6)
        self.assertEqual(y.getRightChild().getLeftChild().key,4)
        self.assertEqual(y.getRightChild().getRightChild().key,3)
        z = build_parse_tree('(1 < 1)')
        self.assertEqual(z.getRootVal(),'<')
        self.assertEqual(z.getLeftChild().key,1)
        self.assertEqual(z.getRightChild().key,1)
        a = build_parse_tree('(not(1 < 1))')
        self.assertEqual(a.getRootVal(),'not')
        self.assertEqual(a.getLeftChild().key,'<')
        self.assertEqual(a.getRightChild(),None)
        self.assertEqual(a.getLeftChild().getLeftChild().key,1)
        self.assertEqual(a.getLeftChild().getRightChild().key,1)
        with self.assertRaises(ValueError):
            build_parse_tree('(1 ? 2)')
        with self.assertRaises(Exception):
            build_parse_tree('((1 + 2)')
        
    def test_tokenize(self):
        self.assertEqual(tokenize('1*(22+3)/5'), ['1', '*', '(', '22', '+', '3', ')', '/', '5'])
        self.assertEqual(tokenize('1  + 1'), ['1', '+', '1'])
        self.assertEqual(tokenize('1 ** 1'), ['1', '**', '1'])
        self.assertEqual(tokenize('1 // 1'), ['1', '//', '1'])
        self.assertEqual(tokenize('244+( 77 / 3) * 4'), ['244', '+', '(','77','/','3',')','*','4'])  
        self.assertEqual(tokenize(''), [])
        self.assertEqual(tokenize('not 342 // ** < <= > >= and or !='),['not','342','//','**','<','<=','>','>=','and','or','!='])

    def test_postordereval(self):
        x = build_parse_tree('(1 + 1)')
        y = build_parse_tree('((10 * 6) + (4 / 4))')
        z = build_parse_tree('(1 < 1)')
        a = build_parse_tree('(not(1 < 1))')
        b = build_parse_tree('((5 < 6) and (5 > 6))')
        c = build_parse_tree('((5 < 6) and (5 > 3))')
        d = build_parse_tree('((5 < 6) or (5 > 6))')
        self.assertEqual(postordereval(x),2)
        self.assertEqual(postordereval(y),61)
        self.assertEqual(postordereval(z),False)
        self.assertEqual(postordereval(a),True)
        self.assertEqual(postordereval(b),False)
        self.assertEqual(postordereval(c),True)
        self.assertEqual(postordereval(d),True)
    
    def test_printexp(self):
        x = build_parse_tree('(1 + 1)')
        y = build_parse_tree('((10 * 6) + (4 / 4))')
        z = build_parse_tree('(1 < 1)')
        a = build_parse_tree('(not(1 < 1))')
        b = build_parse_tree('((5 < 6) and (5 > 6))')
        c = build_parse_tree('((5 < 6) and (5 > 3))')
        d = build_parse_tree('((5 < 6) or (5 > 6))')
        self.assertEqual(printexp(x),'( 1 + 1 )')
        self.assertEqual(printexp(y),'(( 10 * 6 )+( 4 / 4 ))')
        self.assertEqual(printexp(z),'( 1 < 1 )')
        self.assertEqual(printexp(a),'(( 1 < 1 )not ')
        self.assertEqual(printexp(b),'(( 5 < 6 )and( 5 > 6 ))')
        self.assertEqual(printexp(c),'(( 5 < 6 )and( 5 > 3 ))')
        self.assertEqual(printexp(d),'(( 5 < 6 )or( 5 > 6 ))')


if __name__ == '__main__':
    import platform
    print(platform.python_version())
    unittest.main()
