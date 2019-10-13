class Node:
    """Node Class Constructor"""
    def __init__(self,initdata):
        self.__data = initdata
        self.__next = None
        self.__previous = None
    
    #allows directs access to property through object.fieldname
    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @property
    def previous(self):
        return self.__previous

    @data.setter
    def data(self,newdata):
        self.__data = newdata

    @next.setter
    def next(self,newnext):
        self.__next = newnext

    @previous.setter
    def previous(self,newprevious):
        self.__previous = newprevious
    
    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext
    
    def setPrevious(self,newprevious):
        self.previous = newprevious

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous