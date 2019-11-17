from binheap import *
import unittest

class BinaryHeapTests(unittest.TestCase):

    def setUp(self):
        self.minbst = BinHeap(True,10)
        self.maxbst = BinHeap(False,10)
    
    def test_properties(self):
        self.assertEqual(self.minbst.heapList,[0])
        self.assertEqual(self.maxbst.heapList,[0])
        self.assertEqual(self.minbst.current_size,0)
        self.assertEqual(self.maxbst.current_size,0)
        self.assertEqual(self.minbst.isminheap,True)
        self.assertEqual(self.maxbst.isminheap,False)

    def test_insert_min_heap(self):
        self.minbst.insert(1)
        self.assertEqual(self.minbst.heapList,[0,1])
        self.assertEqual(self.minbst.current_size,1)
        self.minbst.insert(20)
        self.minbst.insert(10)
        self.minbst.insert(61)
        self.minbst.insert(2)
        self.minbst.insert(43)
        self.minbst.insert(68)
        self.minbst.insert(23)
        self.minbst.insert(14)
        self.minbst.insert(66)
        self.assertEqual(self.minbst.heapList,[0, 1, 2, 10, 14, 20, 43, 68, 61, 23, 66])
        self.assertEqual(self.minbst.current_size,10)
        self.minbst.insert(15)
        #maxed out size and drops least important value
        self.assertEqual(self.minbst.current_size,10)
        self.assertEqual(self.minbst.heapList,[0, 1, 2, 10, 14, 20, 43, 15, 61, 23, 66])

    def test_insert_max_heap(self):
        self.maxbst.insert(1)
        self.assertEqual(self.maxbst.heapList,[0,1])
        self.assertEqual(self.maxbst.current_size,1)
        self.maxbst.insert(20)
        self.maxbst.insert(10)
        self.maxbst.insert(61)
        self.maxbst.insert(2)
        self.maxbst.insert(43)
        self.maxbst.insert(68)
        self.maxbst.insert(23)
        self.maxbst.insert(14)
        self.maxbst.insert(66)
        self.assertEqual(self.maxbst.heapList,[0, 68, 66, 61, 20, 23, 10, 43, 1, 14, 2])
        self.assertEqual(self.maxbst.current_size,10)
        self.maxbst.insert(15)
        #maxed out size and drops least important value
        self.assertEqual(self.maxbst.current_size,10)
        self.assertEqual(self.maxbst.heapList,[0, 68, 66, 61, 20, 23, 10, 43, 15, 14, 2])

    def test_findlowpriorityindx(self):
        self.minbst.build_heap([ 1, 2, 10, 14, 20, 43, 68, 61, 23, 66])
        self.assertEqual(self.minbst.findlowpriorityindx(self.minbst.current_size // 2 + 1),7)
        self.maxbst.build_heap([ 68, 66, 61, 20, 23, 10, 43, 1, 14, 2])
        self.assertEqual(self.minbst.findlowpriorityindx(self.minbst.current_size // 2 + 1),7)

    def test_build_min_heap(self):
        self.minbst.build_heap([11, 46, 78, 64, 17, 74, 95, 16, 28, 6, 75])
        self.assertEqual(self.minbst.heapList,[0, 6, 11, 74, 16, 17, 78, 75, 64, 28, 46])
        self.minbst.heapList = [0]
        self.minbst.build_heap([11, 46, 78, 64, 17, 74, 95, 16, 28, 6, 75, 44, 31, 13, 2, 5])
        self.assertEqual(self.minbst.heapList,[0, 2, 5, 13, 11, 6, 31, 44, 16, 28, 17])
    
    def test_build_max_heap(self):
        self.maxbst.build_heap([11, 46, 78, 64, 17, 74, 95, 16, 28, 6, 75])
        self.assertEqual(self.maxbst.heapList,[0, 95, 75, 78, 46, 64, 74, 11, 16, 28, 17])
        self.maxbst.heapList = [0]
        self.maxbst.build_heap([11, 46, 78, 64, 17, 74, 95, 16, 28, 6, 75, 104, 222, 104, 111])
        self.assertEqual(self.maxbst.heapList,[0, 222, 111, 95, 104, 104, 74, 78, 46, 75, 64])

    def test_perc_down_min_heap(self):
        self.minbst.build_heap([20,10,23,43,53,12,54,13,64])
        self.minbst.heapList[1] = 30
        self.minbst.perc_down(1,9)
        self.assertEqual(self.minbst.heapList,[0, 12, 13, 23, 20, 53, 30, 54, 43, 64])
        
    def test_perc_down_max_heap(self):
        self.maxbst.build_heap([20,10,23,43,53,12,54,13,64])
        self.maxbst.heapList[1] = 30
        self.maxbst.perc_down(1,9)
        self.assertEqual(self.maxbst.heapList,[0, 54, 53, 30, 43, 20, 12, 23, 13, 10]) 
        
    def test_perc_up_min_heap(self):
        self.minbst.build_heap([20,10,23,43,53,12,54,13,64])
        self.minbst.heapList.append(5)
        self.minbst.current_size += 1
        self.minbst.perc_up(self.minbst.current_size)
        self.assertEqual(self.minbst.heapList,[0, 5, 10, 12, 20, 13, 23, 54, 43, 64, 53])

    def test_perc_up_max_heap(self):
        self.maxbst.build_heap([20,10,23,43,53,12,54,13,64])
        self.maxbst.heapList.append(25)
        self.maxbst.current_size += 1
        self.maxbst.perc_up(self.maxbst.current_size)
        self.assertEqual(self.maxbst.heapList,[0, 64, 53, 54, 43, 25, 12, 23, 13, 10, 20])   

    def test_min_or_max_child(self):
        self.minbst.build_heap([20,10,23,43,53,12,54,13,64])
        self.maxbst.build_heap([20,10,23,43,53,12,54,13,64])
        self.assertEqual(self.minbst.min_or_max_child(1,self.minbst.current_size),3)
        self.assertEqual(self.maxbst.min_or_max_child(1,self.maxbst.current_size),3)

    def test_min_heap_delRoott(self):
        self.minbst.build_heap([20,10,23,43,53,12,54,13,64])
        x = self.minbst.delRoot()
        self.assertEqual(x,10)
        self.assertEqual(self.minbst.heapList,[0, 12, 13, 23, 20, 53, 64, 54, 43])

    def test_min_heap_delRoott(self):
        self.maxbst.build_heap([20,10,23,43,53,12,54,13,64])
        x = self.maxbst.delRoot()
        self.assertEqual(x,64)
        self.assertEqual(self.maxbst.heapList,[0, 54, 53, 23, 43, 20, 12, 10, 13])

    def test_sort_min_heap(self):
        self.minbst.build_heap([20,10,23,43,53,12,54,13,64])
        self.minbst.sort()
        self.assertEqual(self.minbst.heapList,[0, 64, 54, 53, 43, 23, 20, 13, 12, 10])

    def test_sort_max_heap(self):
        self.maxbst.build_heap([20,10,23,43,53,12,54,13,64])
        self.maxbst.sort()
        self.assertEqual(self.maxbst.heapList,[0, 10, 12, 13, 20, 23, 43, 53, 54, 64])

if __name__ == '__main__':
    unittest.main()