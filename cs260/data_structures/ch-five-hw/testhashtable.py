from hashtable import *
import unittest

class TestStringMethods(unittest.TestCase): 
    """Unit tests for Hash Table Exercises
    Arguments:
        unittest {unittest}
    """
    def setUp(self):
        self.hashtable = HashTable()
        self.keys = [randomString() for _ in range(100)]
        
    def test_properties(self):
        """Tests Hashtable object properties""" 
        self.assertEqual(self.hashtable.size, 101) 
        self.assertIsInstance(self.hashtable.slots, list)
        self.assertIsInstance(self.hashtable.data, list)

    def test_setters(self):
        """Tests Hashtable setters"""
        self.hashtable.size = 200
        self.hashtable.slots = [1,2,3]
        self.hashtable.data = [1,2,3]
        self.assertEqual(self.hashtable.size, 200) 
        self.assertEqual(self.hashtable.slots, [1,2,3])
        self.assertEqual(self.hashtable.data, [1,2,3])

    def test_load_factor(self):
        self.assertEqual(self.hashtable.load_factor(), 0)
        for i in range(25):
            self.hashtable.put(self.keys[i],i)
        self.assertEqual(self.hashtable.load_factor(), .25)
        for i in range(26,77):
            self.hashtable.put(self.keys[i],i)
        self.assertEqual(self.hashtable.load_factor(), .76)
        self.hashtable.put(self.keys[78],78)
        self.assertEqual(self.hashtable.load_factor(), .39)

    def test_resize(self):
        for i in range(25):
            self.hashtable.put(self.keys[i],i)
        self.hashtable.resize()
        self.assertEqual(self.hashtable.size,201)
        self.assertEqual(len(self.hashtable),25)
        self.hashtable.resize()
        self.assertEqual(self.hashtable.size,301)
    
    def test_put(self):
        #test basic put
        self.hashtable.put(5415144535,541)
        # test Exception
        
        with self.assertRaises(Exception):
            self.hashtable.put('deleted',1) 
        for i in range(0,77):
            self.hashtable.put(self.keys[i],i)
        #test auto resize
        self.assertEqual(self.hashtable.size,201) 
        self.hashtable.put('apple','banana')
        self.hashtable.put('apple','grapes')
        # test replace
        self.assertEqual(self.hashtable['apple'],'grapes')

    def test_hashfunction(self):
        x = self.hashtable.hashfunction('apple')
        y = self.hashtable.hashfunction(12345)
        self.assertIsInstance(x,int)
        self.assertIsInstance(y,int)

    def test_rehash(self):
        self.assertEqual(self.hashtable.rehash(10,3),19)
        self.assertEqual(self.hashtable.rehash(10,1),11)
        self.assertEqual(self.hashtable.rehash(10,9),91)

    def test_get(self):
        self.assertEqual(self.hashtable.get('apple'),None)
        self.hashtable.put('apple','pear')
        self.assertEqual(self.hashtable.get('apple'),'pear')
        self.assertEqual(self.hashtable.get(124),None)
        self.hashtable.put(124,1234)
        self.assertEqual(self.hashtable.get(124),1234)
    
    def test__delitem__(self):
        self.hashtable.put('apple','pear')
        del self.hashtable['apple']
        self.assertEqual(self.hashtable.get('apple'),None)

    def test__getitem__(self):
        self.hashtable.put('apple','pear')
        self.assertEqual(self.hashtable['apple'],'pear')

    def test__setitem__(self):
        self.hashtable['apple'] = 'pear'
        self.assertEqual(self.hashtable['apple'],'pear')
        self.hashtable['apple'] = 'banana'
        self.assertEqual(self.hashtable['apple'],'banana')

    def test__len__(self):
        self.assertEqual(len(self.hashtable),0)
        for i in range(0,20):
            self.hashtable.put(self.keys[i],i)
        self.assertEqual(len(self.hashtable),20)
    
    def test_keys(self):
        self.assertEqual(self.hashtable.keys(),[])
        self.hashtable.put('a',1)
        self.hashtable.put('b',2)
        self.hashtable.put('c',3)
        self.assertEqual(self.hashtable.keys(),['a','b','c'])
    
    def test_values(self):
        self.assertEqual(self.hashtable.values(),[])
        self.hashtable.put('a',1)
        self.hashtable.put('b',2)
        self.hashtable.put('c',3)
        self.assertEqual(self.hashtable.values(),[1,2,3])

    def test_items(self):
        self.assertEqual(self.hashtable.items(),[])
        self.hashtable.put('a',1)
        self.hashtable.put('b',2)
        self.hashtable.put('c',3)
        self.assertEqual(self.hashtable.items(),[('a',1),('b',2),('c',3)])

if __name__ == '__main__':
    unittest.main()