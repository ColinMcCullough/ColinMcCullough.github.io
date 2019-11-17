'''
Exercise # 6: Create a binary heap with a limited heap size. In other words, the heap only keeps track
of the n most important items. If the heap grows in size to more than n items the least
important item is dropped.
>>

Exercise # 8: Using the build_heap method, write a sorting function that can sort a list in 𝑂(𝑛 log 𝑛)
time.
>> See sort() method

Exercise # 10: Implement a binary heap as a max heap.
>> Current heap can be toggled between max or min heap with first boolean param

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
    def __init__(self, heaptype = True, maxsize = 10):
        """Constructor
        Keyword Arguments:
            heaptype {bool} -- True for min heap, false for max heap (default: {True})
            maxsize {bool} -- Max size of heap, drops lowest priority after (default: {10})
        """
        self.__heapList = [0]
        self.__current_size = 0
        self.__max_size = maxsize
        self.__isminheap = heaptype
        self.greater_min_less_max = lambda a,b: a > b if self.isminheap else a < b
        self.less_min_greater_max = lambda a,b: a < b if self.isminheap else a > b

    @property
    def heapList(self):
        return self.__heapList
    
    @property
    def current_size(self):
        return self.__current_size
    
    @property
    def max_size(self):
        return self.__max_size

    @property
    def isminheap(self):
        return self.__isminheap

    @current_size.setter
    def current_size(self, newsize):
        """ current_size property setter
        Arguments: newsize {int} 
        """
        self.__current_size = newsize
    
    @heapList.setter
    def heapList(self, newlist):
        """ current_size property setter
        Arguments: newsize {int} 
        """
        self.__heapList = newlist

    def insert(self, k):
        """Inserts item into its correct position following the Heap Order Property
        Arguments:
            k {Object}
        """
        if self.current_size >= self.max_size:
            lowest_priority_indx = self.findlowpriorityindx(self.current_size // 2 + 1)
            if self.greater_min_less_max(self.heapList[lowest_priority_indx],k):
                self.heapList[lowest_priority_indx] = k
                self.perc_up(lowest_priority_indx)
        else:
            self.heapList.append(k)
            self.current_size += 1
            self.perc_up(self.current_size)
    
    def findlowpriorityindx(self,pos):
        """Returns the index position of the lowest priority item
        in the heaplist.
        Arguments:
            pos {int} -- start position in list to 
                iteratate towards end of list from
        
        Returns:
            [int] -- index of position in heaplist property 
                with lowest priority
        """        
        lowindx = pos
        while pos < self.current_size:
            if self.greater_min_less_max(self.heapList[pos+1],self.heapList[lowindx]):
                lowindx = pos + 1
            pos += 1    
        return lowindx
    

    def build_heap(self, alist):
        """Builds heap following the Heap Order Property
        Arguments:
            alist {List}
        """
        #list is shorter than max size
        if len(alist) - 1 + self.current_size < self.max_size:
            self.current_size = len(alist) + self.current_size
            self.heapList += alist[:]
            i = len(alist) // 2

            while i > 0:
                self.perc_down(i,self.current_size)
                i -= 1
        else: #list is longer than max size
            self.current_size = self.max_size
            i = self.max_size // 2
            self.heapList = [0] + alist[:self.max_size]
            while i > 0:
                self.perc_down(i,self.current_size)
                i -= 1
            for i in range(self.max_size,len(alist),1):
                self.insert(alist[i])


    def perc_down(self, i,size):
        """Moves element into place following the Heap Order Property
        Arguments:
            i {int} -- index of elemement to be moved
            size {int} -- length of list
        """
        while (i * 2) <= size:
            mc = self.min_or_max_child(i,size)
            if self.greater_min_less_max(self.heapList[i],self.heapList[mc]):
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]

            i = mc

    def perc_up(self, i):
        """Moves element into place following the Heap Order Property
        Arguments:
            i {int} -- index of elemement to be moved
        """
        while i // 2 > 0:
            if self.less_min_greater_max(self.heapList[i],self.heapList[i // 2]):
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]

            i = i // 2

    def min_or_max_child(self, i,size):
        """Finds index of min child if min heap, max child if max heap
        Arguments:
            i {int} -- index of parent
        Returns
            i {int} -- index of min child if min heap, max child if max heap
        """
        if i * 2 + 1 > size:
            return i * 2
        else:
            if self.less_min_greater_max(self.heapList[i * 2] ,self.heapList[i * 2 + 1]):
                return i * 2
            else:
                return i * 2 + 1
    
    def delRoot(self):
        """Removes Root element and restores the Heap Order Property
        Returns:
            Root Element {Object}
        """
        if self.current_size == 0:
            raise IndexError('no root to delete')
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.current_size]
        self.current_size -= 1
        self.heapList.pop()
        self.perc_down(1,self.current_size)
        return retval

    def sort(self):
        """ Sorts instance property heaplist by descending if
            min heap and ascending if max heap
        """
        size = self.current_size
        for i in range(size,1,-1): 
            self.heapList[1],self.heapList[size] = self.heapList[size],self.heapList[1]
            size -= 1
            self.perc_down(1,size)
        