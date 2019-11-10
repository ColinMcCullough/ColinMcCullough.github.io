from circular_dbl_linked_list import CircularDoubleLinkedList
from node import Node
import unittest 

class TestStringMethods(unittest.TestCase): 
    """Unit tests for CircularDoubleLinkedList Class
    Arguments:
        unittest {unittest}
    """
    def setUp(self):
        """Sets up Node CircularDoubleLinkedList to be tested""" 
        self.cdll = CircularDoubleLinkedList()
    
    def test_properties(self):
        """Tests CircularDoubleLinkedList object properties""" 
        self.assertEqual(self.cdll.head, None)
        self.assertEqual(self.cdll.size, 0)
    
    def test_head_setter(self):
        """Tests CircularDoubleLinkedList head setter"""
        self.cdll.head = Node('a')
        self.assertEqual(self.cdll.head.getData(), 'a')
        self.assertEqual(self.cdll.size, 0)
    
    def test_size_setter(self):
        """Tests CircularDoubleLinkedList size setter"""
        self.assertEqual(self.cdll.size, 0)
        self.cdll.size = 1
        self.assertEqual(self.cdll.size, 1)
    
    def test_size_getter(self):
        """Tests CircularDoubleLinkedList size getter"""
        self.assertEqual(self.cdll.getSize(), 0)
        self.cdll.size = 1
        self.assertEqual(self.cdll.getSize(), 1)

    def test_decrementSize(self):
        """Tests CircularDoubleLinkedList decrementSize"""
        self.cdll.size = 3
        self.cdll.decrementSize()
        self.assertEqual(self.cdll.getSize(), 2)
        self.cdll.size = 0
        with self.assertRaises(Exception):
            self.cdll.decrementSize()

    def test_incrementSize(self):
        """Tests CircularDoubleLinkedList incrementSize"""
        self.cdll.incrementSize()
        self.assertEqual(self.cdll.getSize(), 1)
        self.cdll.incrementSize()
        self.assertEqual(self.cdll.getSize(), 2)


    def test_is_empty(self):
        """Tests CircularDoubleLinkedList isEmpty method"""
        self.assertEqual(self.cdll.isEmpty(), True)
        self.cdll.add('a')
        self.assertEqual(self.cdll.isEmpty(), False)
    
    def test_search(self):
        """Tests CircularDoubleLinkedList search method"""
        self.assertEqual(self.cdll.search('a'), False)
        self.cdll.add('a')
        self.assertEqual(self.cdll.search('a'), True)

    def test_add(self):
        """Tests CircularDoubleLinkedList add method"""
        self.cdll.add('a')
        self.assertEqual(self.cdll.head.getData(), 'a')
        self.assertEqual(self.cdll.getSize(), 1)
        self.cdll.add('b')
        self.assertEqual(self.cdll.head.getData(), 'b')
        self.assertEqual(self.cdll.getSize(), 2)
        self.cdll.add('c')
        self.assertEqual(self.cdll.head.getData(), 'c')
        self.assertEqual(self.cdll.getSize(), 3)
    
    def test_append(self):
        """Tests CircularDoubleLinkedList append method"""
        self.cdll.append('a')
        self.assertEqual(self.cdll.head.getPrevious().getData(), 'a')
        self.assertEqual(self.cdll.getSize(), 1)
        self.cdll.append('b')
        self.assertEqual(self.cdll.head.getPrevious().getData(), 'b')
        self.assertEqual(self.cdll.getSize(), 2)
        self.cdll.append('c')
        self.assertEqual(self.cdll.head.getPrevious().getData(), 'c')
        self.assertEqual(self.cdll.getSize(), 3)
    
    def test_deletefirst(self):
        """Tests CircularDoubleLinkedList deletefirst method"""
        with self.assertRaises(Exception):
            self.cdll.deletefirst()
        self.cdll.add('a')
        self.cdll.deletefirst()
        self.assertEqual(self.cdll.head, None)
        self.assertEqual(self.cdll.getSize(), 0)
        self.cdll.add('b')
        self.cdll.add('c')
        self.cdll.deletefirst()
        self.assertEqual(self.cdll.head.getData(), 'b')
        self.assertEqual(self.cdll.getSize(), 1)

    def test_pop(self):
        """Tests CircularDoubleLinkedList pop method"""
        with self.assertRaises(Exception):
            self.cdll.pop()
        self.cdll.add('a')
        self.cdll.pop()
        self.assertEqual(self.cdll.head, None)
        self.assertEqual(self.cdll.getSize(), 0)
        self.cdll.add('b')
        self.cdll.add('c')
        self.cdll.pop()
        self.assertEqual(self.cdll.head.getData(), 'c')
        self.assertEqual(self.cdll.getSize(), 1)

    def test_popbyindex(self):
        """Tests CircularDoubleLinkedList popbyindex method"""
        with self.assertRaises(IndexError):
            self.cdll.popbyindex(0)
        self.cdll.add('a')
        self.cdll.popbyindex(0)
        self.assertEqual(self.cdll.head, None)
        self.assertEqual(self.cdll.getSize(), 0)
        self.cdll.add('c')
        self.cdll.add('b')
        self.cdll.add('a')
        self.cdll.popbyindex(1)
        self.assertEqual(self.cdll.head.getData(), 'a')
        self.assertEqual(self.cdll.head.getNext().getData(), 'c')
        self.assertEqual(self.cdll.head.getPrevious().getData(), 'c')
        self.assertEqual(self.cdll.getSize(), 2)
    
    def test_remove(self):
        """Tests CircularDoubleLinkedList remove method"""
        with self.assertRaises(Exception):
            self.cdll.remove('a')
        self.cdll.add('a')
        self.cdll.remove('a')
        self.assertEqual(self.cdll.head, None)
        self.assertEqual(self.cdll.getSize(), 0)
        self.cdll.add('c')
        self.cdll.add('b')
        self.cdll.add('a')
        self.cdll.remove('a')
        self.assertEqual(self.cdll.head.getData(), 'b')
        self.assertEqual(self.cdll.head.getNext().getData(), 'c')
        self.assertEqual(self.cdll.head.getPrevious().getData(), 'c')
        self.assertEqual(self.cdll.getSize(), 2)
    
    def test_get_node(self):
        """Tests CircularDoubleLinkedList get_node method"""
        with self.assertRaises(Exception):
            self.cdll.get_node(0)
        self.cdll.add('c')
        with self.assertRaises(Exception):
            self.cdll.get_node(-1)
        self.cdll.add('b')
        self.cdll.add('a')
        self.assertEqual(self.cdll.get_node(0).getData(), 'a')
        self.assertEqual(self.cdll.get_node(1).getData(), 'b')
        self.assertEqual(self.cdll.get_node(2).getData(), 'c')

    def test_insert(self):
        """Tests CircularDoubleLinkedList insert method"""
        with self.assertRaises(IndexError):
            self.cdll.insert(-1,"a")
        self.cdll.add('d')
        self.cdll.add('c')
        self.cdll.add('b')
        self.cdll.add('a')
        self.assertEqual(self.cdll.getSize(), 4)
        with self.assertRaises(IndexError):
            self.cdll.insert(5,"a")
        self.cdll.insert(4,"z")
        self.assertEqual(self.cdll.index('z'), 4)
        self.assertEqual(self.cdll.head.getPrevious().getData(),'z')
        self.assertEqual(self.cdll.getSize(), 5)
        self.cdll.insert(0,"r")
        self.assertEqual(self.cdll.index('r'), 0)
        self.assertEqual(self.cdll.head.getData(),'r')
        self.assertEqual(self.cdll.getSize(), 6)
        self.cdll.insert(1,"l")
        self.assertEqual(self.cdll.index('l'), 1)
        self.assertEqual(self.cdll.head.getNext().getData(),'l')
        self.assertEqual(self.cdll.getSize(), 7)
    
    def test_str_overload(self):
        self.assertEqual(str(self.cdll),"[]")
        self.cdll.add('d')
        self.cdll.add('c')
        self.cdll.add('b')
        self.cdll.add('a')
        self.assertEqual(str(self.cdll),"[a,b,c,d]")

if __name__ == '__main__':
    unittest.main()