from queue import Queue
'''
Implement a radix sorting machine. A radix sort for base 10 integers is a mechanical sorting 
technique that utilizes a collection of bins, one main bin and 10 digit bins. Each bin acts 
like a queue and maintains its values in the order that they arrive. The algorithm begins by 
placing each number in the main bin. Then it considers each value digit by digit. The first value 
is removed and placed in a digit bin corresponding to the digit being considered. For example, 
if the ones digit is being considered, 534 is placed in digit bin 4 and 667 is placed in digit bin 7. 
Once all the values are placed in the corresponding digit bins, the values are collected from bin 0 to bin 9 
and placed back in the main bin. The process continues with the tens digit, the hundreds, and so on. 
After the last digit is processed, the main bin contains the values in order.
'''
class RadixSort:
    def __init__(self,lst):
        """[Initialized properties]
        Arguments: lst {List} -- List of type int
        """
        if not isinstance(lst,list):
            raise TypeError('must pass in a list')
        for i in range(len(lst)):
            if not isinstance(lst[i],int):
                raise TypeError('list must hold integers only')
        self.__lst = self.list_int_to_str(lst)
        self.__mainqueue = self.createMainQueue()
        self.__binsqueue = self.createTenBinsInLst()
        self.__maxnum = max(lst)
        
    @property
    def lst(self):
        return self.__lst
    
    @property
    def maxnum(self):
        return self.__maxnum

    @property
    def mainqueue(self):
        return self.__mainqueue

    @property
    def binsqueue(self):
        return self.__binsqueue

    @lst.setter
    def lst(self,newlst):
        self.__lst = newlst
    
    def getMaxNum(self):
        """
        Returns: {Integer} -- returns maxnum property
        """
        return self.maxnum

    
    def list_int_to_str(self,lst):
        """converts list of int to list of string
        Arguments: lst {List} -- List of integers
        Returns: {List} -- List of strings
        """
        return [str(i) for i in lst]

    def list_str_to_int(self,lst):
        """converts list of string to list of int
        Arguments: lst {List} -- List of strings
        Returns: {List} -- List of int
        """
        return [int(i) for i in lst]
    
    def createMainQueue(self):
        """
        Initializes mainqueue propert by placing each item from list in into it
        Returns: {Queue}
        """
        q = Queue()
        for num in self.lst:
            q.enqueue(num)
        return q

    
    def createTenBinsInLst(self):
        """
        Create a list of Queues and initialize them with index 0 to 9
        Returns: {List} - An empty queue object is in each index position
        """
        lst = []
        for i in range(10):
            lst.append(Queue())
        return lst

    def sort(self):
        """
            Main function for class. Sorts list passed in and returns list in sorted order
            Returns: {List} -- Sorted smallest to largest
        """
        for i in range(1, self.maxnum + 1):
            already_used = []
            while not self.mainqueue.isEmpty():
                num = self.mainqueue.dequeue()
                if i > len(num):
                    already_used.append(num)
                    continue
                current_que_num = int(num[len(num) - i])
                correct_bin = self.binsqueue[current_que_num]
                correct_bin.enqueue(num)
            for used in already_used:
                self.mainqueue.enqueue(used)
            for i in range(len(self.binsqueue)):
                while not self.binsqueue[i].isEmpty():
                    self.mainqueue.enqueue(self.binsqueue[i].dequeue())
        sorted_list = []
        while not self.mainqueue.isEmpty():
            sorted_list.append(self.mainqueue.dequeue())
        return self.list_str_to_int(sorted_list)
