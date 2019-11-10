from node import Node
import unittest 

class TestStringMethods(unittest.TestCase): 
    """Unit tests for Node Class
    Arguments:
        unittest {unittest}
    """
    def setUp(self):
        """Sets up Node properties to be tested""" 
        self.nodeone = Node('a')

    def test_properties(self):
        """Tests Node object properties""" 
        self.assertEqual(self.nodeone.data, 'a')
        self.assertEqual(self.nodeone.next, None)
        self.assertEqual(self.nodeone.previous, None)

    def test_data_setter(self):
        """Tests Node data Setter""" 
        self.nodeone.setData('b')
        self.assertEqual(self.nodeone.data, 'b')
        self.assertEqual(self.nodeone.getData(), 'b')
    
    def test_next_setter(self):
        """Tests Node next Setter""" 
        self.nodeone.setNext(Node('b'))
        self.assertEqual(self.nodeone.getNext().getData(), 'b')
        self.assertEqual(self.nodeone.getNext().data, 'b')
    
    def test_previous_setter(self):
        """Tests Node previous Setter""" 
        self.nodeone.setPrevious(Node('c'))
        self.assertEqual(self.nodeone.getPrevious().getData(), 'c')
        self.assertEqual(self.nodeone.getPrevious().data, 'c')

    def test_data_getter(self):
        """Tests Node data getter""" 
        self.assertEqual(self.nodeone.getData(), 'a')
    
    def test_next_getter(self):
        """Tests Node next getter""" 
        self.nodeone.setNext(Node('b'))
        self.assertEqual(self.nodeone.getNext().getData(), 'b')
    
    def test_previous_getter(self):
        """Tests Node previous getter""" 
        self.nodeone.setPrevious(Node('c'))
        self.assertEqual(self.nodeone.getPrevious().getData(), 'c')


if __name__ == '__main__':
    unittest.main()