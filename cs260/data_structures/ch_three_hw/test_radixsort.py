from radixsort import RadixSort
from queue import Queue
import unittest 

class TestStringMethods(unittest.TestCase): 
    """Unit tests for RadixSort Class
    Arguments:
        unittest {unittest}
    """
    def setUp(self):
        """Sets up RadixSort properties to be tested""" 
        self.rdxsortone = RadixSort([12,43,1,545,21,2,7,4,2,8])
    
    def test_properties(self):
        """Tests RadixSort object properties""" 
        self.assertEqual(self.rdxsortone.lst, ['12','43','1','545','21','2','7','4','2','8'])
        self.assertEqual(isinstance(self.rdxsortone.mainqueue,Queue), True)
        self.assertEqual(self.rdxsortone.mainqueue.isEmpty(), False)
        self.assertEqual(self.rdxsortone.mainqueue.size(), 10)
        self.assertEqual(isinstance(self.rdxsortone.binsqueue,list), True)
        self.assertEqual(len(self.rdxsortone.binsqueue), 10)
        self.assertEqual(self.rdxsortone.maxnum, 545)
        with self.assertRaises(TypeError):
            RadixSort('12,1,3,45,6,6')
        with self.assertRaises(TypeError):
            RadixSort([12,1.1,3,45,6,6])
        
    def test_list_int_to_str(self):
        """Test RadixSort object list int to string method"""
        self.assertEqual(self.rdxsortone.list_int_to_str([1,2,3,4,5,6]),['1','2','3','4','5','6'])

    def test_list_str_to_int(self):
        """Test RadixSort object list string to int method"""
        self.assertEqual(self.rdxsortone.list_str_to_int(['1','2','3','4','5','6']),[1,2,3,4,5,6])

    def test_sort(self):
        """Test RadixSort object sort method"""
        self.assertEqual(self.rdxsortone.sort(),[1, 2, 2, 4, 7, 8, 12, 21, 43, 545])
        radix2 = RadixSort([324,1232,2,32,5,1,32454,3,1,99])
        self.assertEqual(radix2.sort(),[1, 1, 2, 3, 5, 32, 99, 324, 1232, 32454])

if __name__ == '__main__':
    unittest.main()