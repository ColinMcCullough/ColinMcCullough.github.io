import unittest
from quicksort import *
import random
import copy

class TestStringMethods(unittest.TestCase): 
    """Unit tests for Binary Search Exercises
    Arguments:
        unittest {unittest}
    """
    def setUp(self):
        self.lst = list(reversed(range(10)))
    
    def test_time_me(self):
        @time_me
        def test(a,b,c):
            return a+b+c
        self.assertIsInstance(test(1,2,3),float)
    
    def test_quickSort(self):
        quickSort(self.lst,0,9)
        self.assertEqual(self.lst,[0,1,2,3,4,5,6,7,8,9])
        alist  = [random.randint(0,100) for _ in range(100)]
        alist2 = copy.deepcopy(alist)
        quickSort(alist,0,len(alist)-1)
        alist2.sort()
        self.assertEqual(alist,alist2)

    def test_quickSortWithMedian3(self):
        quickSortWithMedian3(self.lst,0,9)
        self.assertEqual(self.lst,[0,1,2,3,4,5,6,7,8,9])
        alist  = [random.randint(0,100) for _ in range(100)]
        alist2 = copy.deepcopy(alist)
        quickSortWithMedian3(alist,0,len(alist)-1)
        alist2.sort()
        self.assertEqual(alist,alist2)

    def test_quickSortWithInsertion(self):
        quickSortWithInsertion(self.lst,0,9)
        self.assertEqual(self.lst,[0,1,2,3,4,5,6,7,8,9])
        alist  = [random.randint(0,100) for _ in range(100)]
        alist2 = copy.deepcopy(alist)
        quickSortWithInsertion(alist,0,len(alist)-1)
        alist2.sort()
        self.assertEqual(alist,alist2)

    def test_median(self):
        self.assertEqual(median((1,0),(2,1),(3,2)),(2,1))
        self.assertEqual(median((5,0),(50,10),(100,20)),(50,10))
        self.assertEqual(median((134,0),(234,10),(50,20)),(134,0))
        
    def test_partition_median_3(self):
        lst = [34,23,12,34,66,34,87,34,95,55]
        self.assertEqual(partition_median_3(lst,0,9),6)
        self.assertEqual(lst,[34, 23, 12, 34, 34, 34, 55, 87, 95, 66])
        lst2 = [9,8,7,6,5,4,3,2,1]
        self.assertEqual(partition_median_3(lst2,0,8),4)
        self.assertEqual(lst2,[4, 1, 2, 3, 5, 9, 6, 7, 8])

    def test_partition(self):
        lst = [45,23,12,34,66,34,87,34,95,55]
        self.assertEqual(partition([1,2,3,4,5,6],0,5),0)
        self.assertEqual(partition(lst,0,9),5)
        self.assertEqual(lst,[34,23,12,34,34,45,87,66,95,55])

    def insertionSort(self):
        insertionSort(self.lst,0,9)
        self.assertEqual(self.lst,[0,1,2,3,4,5,6,7,8,9])
        alist  = [random.randint(0,100) for _ in range(100)]
        alist2 = copy.deepcopy(alist)
        insertionSort(alist,0,len(alist)-1)
        alist2.sort()
        self.assertEqual(alist,alist2)

        


if __name__ == '__main__':
    unittest.main()