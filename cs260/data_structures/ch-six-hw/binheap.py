'''
Exercise # 6: Create a binary heap with a limited heap size. In other words, the heap only keeps track
of the n most important items. If the heap grows in size to more than n items the least
important item is dropped.

Exercise # 8: Using the build_heap method, write a sorting function that can sort a list in 𝑂(𝑛 log 𝑛)
time.

Exercise # 10: Implement a binary heap as a max heap.

Exercise # 11: Using the BinaryHeap class, implement a new class called PriorityQueue. Your
PriorityQueue class should implement the constructor, plus the enqueue and
dequeue methods.

'''

# this heap takes key value pairs, we will assume that the keys are integers
class BinHeap:
    """Binary Heap Abstract Class
    Interface:
        build_heap(list)
        perc_down(index)
        perc_up(index)
        min_or_max_child(index) 
        delRoot()
        sort()
    """
    def __init__(self,heaptype = True,maxsize = 10):
        """Constructor
        Keyword Arguments:
            heaptype {bool} -- True for min heap, false for max heap (default: {True})
            maxsize {bool} -- Max size of heap, drops lowest priority after (default: {10})
        """
        self.__heapList = [0]
        self.__current_size = 0
        self.__max_size = maxsize
        self.__isminheap = heaptype
        self.pdowncompare = lambda a,b: a > b if self.isminheap else a < b
        self.pupcompare = lambda a,b: a < b if self.isminheap else a > b

    @property
    def heapList(self):
        return self.__heapList
    
    @property
    def current_size(self):
        return self.__current_size
    
    @property
    def maxsize(self):
        return self.__maxsize

    @property
    def isminheap(self):
        return self.__isminheap

    @current_size.setter
    def current_size(self,newsize):
        """ current_size property setter
        Arguments: newsize {int} 
        """
        self.__current_size = newsize
    
    @heapList.setter
    def heapList(self,newlist):
        """ current_size property setter
        Arguments: newsize {int} 
        """
        self.__heapList = newlist

    def build_heap(self, alist):
        """Builds heap following the Heap Order Property
        Arguments:
            alist {List}
        """
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heapList = [0] + alist[:]

        while i > 0:
            self.perc_down(i)
            i = i - 1

    def perc_down(self, i):
        """Moves element into place following the Heap Order Property
        Arguments:
            i {int} -- index of elemement to be moved
        """
        while (i * 2) <= self.current_size:
            mc = self.min_or_max_child(i)
            if self.pdowncompare(self.heapList[i],self.heapList[mc]):
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]

            i = mc

    def min_or_max_child(self, i):
        """Finds index of min child if min heap, max child if max heap
        Arguments:
            i {int} -- index of parent
        Returns
            i {int} -- index of min child if min heap, max child if max heap
        """
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.pupcompare(self.heapList[i * 2] ,self.heapList[i * 2 + 1]):
                return i * 2
            else:
                return i * 2 + 1

    def perc_up(self, i):
        """Moves element into place following the Heap Order Property
        Arguments:
            i {int} -- index of elemement to be moved
        """
        while i // 2 > 0:
            if self.pupcompare(self.heapList[i],self.heapList[i // 2]):
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]

            i = i // 2
    
    def delRoot(self):
        """Removes Root element and restores the Heap Order Property
        Returns:
            Root Element {Object}
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.current_size]
        self.current_size = self.current_size - 1
        self.heapList.pop()
        self.perc_down(1)
        return retval

    def sort(self):
        """ Sorts instance property heaplist by ascending if
            min heap and descending if max heap
        """
        new_lst = [0]
        for i in range(self.current_size,1,-1): 
            new_lst.append(self.delRoot())
        self.heapList = new_lst
        