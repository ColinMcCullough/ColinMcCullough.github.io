from node import Node

class CircularDoubleLinkedList:
    """Constructor"""
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    @property
    def head(self):
        return self.__head
    
    @property
    def size(self):
        return self.__size

    @head.setter
    def head(self,newref):
        self.__head = newref

    @size.setter
    def size(self,newsize):
        self.__size = newsize

    def isEmpty(self):
        """ Checks if list is empty, returns true if is false if not
            Return {Boolean}
        """
        return self.head == None

    def getSize(self):
        """[Returns size instance field]"""
        return self.size

    def decrementSize(self):
        '''Decreases instance field size by 1'''
        if self.size < 1:
            raise Exception('Size cannot less than 0')
        self.size = self.size - 1

    def incrementSize(self):
        '''Increases instance field size by 1'''
        self.size = self.size + 1

    def search(self,item):
        """Searches for object in node data fields
        Arguments: item {Object}
        Return: {Boolean}
        """
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def add(self,item):
        """Adds new node with item from param at the beginning of list
        Arguments:
            item {Object} -- item to be added 
        """
        newnode = Node(item)
        if self.isEmpty():
            self.head = newnode
            self.head.setPrevious(newnode)
            self.head.setNext(newnode)
        else:
            last = self.head.getPrevious()
            last.setNext(newnode)
            newnode.setPrevious(last)
            newnode.setNext(self.head)
            self.head.setPrevious(newnode)
            self.head = newnode
        self.incrementSize()
    
    def append(self,item):
        """Adds new node with item from param at the end of list
        Arguments:
            item {Object} -- item to be added 
        """
        newnode = Node(item)
        if self.isEmpty():
            self.head = newnode
            self.head.setPrevious(newnode)
            self.head.setNext(newnode)
        else:
            last_node = self.head.getPrevious()
            last_node.setNext(newnode)
            newnode.setPrevious(last_node)
            newnode.setNext(self.head)
            self.head.setPrevious(newnode)
        self.incrementSize()

    def deletefirst(self):
        """Removed first node from list"""
        if self.isEmpty():
            raise Exception('This list is empty')
        lastNode =self.head.getPrevious()
        secondNode = self.head.getNext()
        if self.getSize() > 1:
            secondNode.setPrevious(lastNode)
            lastNode.setNext(secondNode)
            self.head = secondNode
        else:
            self.head = None
        self.decrementSize()

    def pop(self):
        """ Removes last item in list
        Return: {Object} Last item in list 
        """
        if self.isEmpty():
            raise Exception('This list is empty')
        last_node = self.head.getPrevious()
        second_to_last_node = last_node.getPrevious()
        if self.getSize() > 1:
            self.head.setPrevious(second_to_last_node)
            second_to_last_node.setNext(self.head)
        else:
            self.head = None
        self.decrementSize()
        return last_node.getData()

    def popbyindex(self,index):
        """ Removes item by index pos in list
        Arguments: {Integer} - index to remove item from
        Return: {Object} Item in index pos from param 
        """
        if index >= self.getSize() or index < 0:
            raise IndexError('Index out of bounds')
        data = None
        if index == 0 :
            data = self.head.getData()
            self.deletefirst()
                
        elif index == self.getSize() -1:
            data = self.pop()
        else:
            popnode = self.get_node(index)
            beforenode = popnode.getPrevious()
            afternode = popnode.getNext()
            beforenode.setNext(afternode)
            afternode.setPrevious(beforenode)
            data = popnode.getData()
            self.decrementSize()
        return data

    def remove(self,item):
        """ Removes item by data match in list
        Arguments: {Object} - item to remove from list
        """
        current = self.head
        found = False
        index = 0
        while not found and index < self.getSize():
            if current.getData() == item:
                found = True              
            else:
                current = current.getNext()
                index += 1   
        if found:
            if index == 0 :
                self.deletefirst()
            elif index == self.getSize() -1:
                self.pop()
            else:
                before = current.getPrevious()
                after = current.getNext()
                before.setNext(after)
                after.setPrevious(before)
                current.setNext(None)
                current.setPrevious(None)
                self.decrementSize()
        else:
            raise Exception('item not found')

    def get_node(self,index):
        """Gets reference to node at a specified index
        Arguments:
            index {Integer}
        """
        if index < 0 or index >= self.getSize(): 
            raise Exception("This index is out of Bounds")
        current_node = self.head
        i = 0
        while i < index:
            current_node = current_node.getNext()
            i += 1
        return current_node
        
    
    def insert(self,index,item):
        """Adds item to list at specific index   
        Arguments:
            index {Integer} 
            item {Object}
        """
        if index > self.getSize() or index < 0:
            raise IndexError('Index out of bounds')
        new_node = Node(item)
        if self.isEmpty(): 
            self.add(item)
        elif index == self.getSize():
            self.append(item)
        elif index == 0:
            self.add(item)
        else:
            beforenode = self.get_node(index).getPrevious()
            afternode = beforenode.getNext()
            new_node.setNext(afternode)
            new_node.setPrevious(beforenode)
            beforenode.setNext(new_node)
            afternode.setPrevious(new_node)
            self.incrementSize()

    def index(self,item):
        """Looks for index of item in a list. Returns -1 if not found
        Arguments:
            item {Object}
        Returns: {Integer} --  Index position of item or -1 if not found
        """
        current = self.head
        current_index = 0
        found = False
        found_index = -1
        while not found and current_index < self.getSize():
            if current.getData() == item:
                found = True
                found_index = current_index
            else:
                current = current.getNext()
            current_index += 1
        return found_index
            
    def __str__(self):
        """ String representation of current data in list
        Returns: {String}
        """
        string = ''
        current = self.head
        index = 0
        while index < self.getSize():
            string += f'{current.getData()},'
            current = current.getNext()
            index += 1
        return f'[{string[:-1]}]'
    
