#from binheap import BinHeap
from cs260.data_structures.ch_six_hw.binheap import BinHeap

'''
Exercise # 11: Using the BinaryHeap class, implement a new class called PriorityQueue. Your
PriorityQueue class should implement the constructor, plus the enqueue and
dequeue methods.
'''

class PriorityQueue:
    """
        Interface:
            enqueue(item): - inserts item into queue in correct position
            dequeue(item): - removes highest priority item
            size() - size of priority queue
    """
    def __init__(self):
        """Constructor"""
        self.__queue = BinHeap()

    @property
    def queue(self):
        return self.__queue

    def enqueue(self,item):
        """Inserts item into the priority queue
        Arguments:
            item {Object} 
        """        
        self.queue.insert(item)

    def dequeue(self):
        """Removes the highest priority item from the priority queue
        Returns:
            item {Object} 
        """  
        return self.queue.delRoot()
    
    def size(self):
        """Number of items in queue
        Returns:
            [int] -- number of items in queue
        """        
        return self.queue.current_size

    def decreaseKey(self,val,amt):
        
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.current_size:
            if self.heapList[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapList[myKey] = (amt,self.heapList[myKey][1])
            self.percUp(myKey)
