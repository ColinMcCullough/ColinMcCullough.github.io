import random
import string
import math
'''
Exercise # 4:
Implement the len method (__len__) for the hash table Map ADT implementation.(number of key-value pairs)

Exercise # 5:
How can you delete items from a hash table that uses chaining for collision resolution?
How about if open addressing is used? What are the special circumstances that must be
handled? Implement the del method for the HashTable class.

Answer: To delete an items from a hash table that uses chaining for collision resolution simply implement 
a linked list with a delete method and remove the reference to that index. That way if there is a collision you can still
just add on to the end of the linked list and when searching items, it can iterate until the end of the linked list

Exercise # 6:
In the hash table map implementation, the hash table size was chosen to be 101. If the
table gets full, this needs to be increased. Re-implement the put method so that the table
will automatically resize itself when the loading factor reaches a predetermined value
(you can decide the value based on your assessment of load versus performance).

Exercise # 7:
Implement quadratic probing as a rehash technique.
'''


class HashTable:
    """Hashtable Class"""
    def __init__(self):
        """constructor"""
        self.__size = 101
        self.__slots = [None] * self.size
        self.__data = [None] * self.size

    
    @property
    def size(self):
        return self.__size
    @property
    def slots(self):
        return self.__slots
    @property
    def data(self):
        return self.__data

    @size.setter
    def size(self,newsize):
        """ size property setter
        Arguments: newsize {Int}
        """
        self.__size = newsize
    
    @slots.setter
    def slots(self,newkeys):
        """ Slots property setter
        Arguments: newkeys {Object}
        """
        self.__slots = newkeys
    
    @data.setter
    def data(self,newdata):
        """ Data property setter
        Arguments: newdata {Object}
        """
        self.__data = newdata

    def load_factor(self):
        """Gets current load factor of HashTable
        Returns: {Float}
        """
        load = len(self) / self.size
        return math.ceil(load*100)/100

    def resize(self):
        """Resizes table by adding 100 additional spaces"""
        self.size += 100
        currentdata = self.items()
        self.slots = [None] * self.size
        self.data = [None] * self.size
        for key,value in currentdata:
            self.put(key,value)
    
    def put(self,key,data):
        """ Adds new items to hash table
        Arguments:
            key {Object}
            data {Object}
        """
        if key == 'deleted':
            raise Exception('deleted is a reserved keyword and cant be used as a key')
        if self.load_factor() > 0.75:
            self.resize()
        hashvalue = self.hashfunction(key)
        collisions = 0
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                collisions += 1
                nextslot = self.rehash(hashvalue,collisions)
                while self.slots[nextslot] != None and self.slots[nextslot] != 'deleted' and self.slots[nextslot] != key:
                    collisions += 1
                    nextslot = self.rehash(nextslot,collisions)

                if self.slots[nextslot] == None or self.slots[nextslot] == 'deleted':
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace

    def hashfunction(self,key):
        """Responsible for putting data into hash table      
        Arguments: key {Object}
        """
        key = str(key) if not isinstance(key,str) else key
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos]) * pos + 1
        return sum%self.size

    def rehash(self,oldhash,step):
        """Rehash function 
        Arguments:oldhash {int}, step {int}
        """
        return (oldhash + (step**2))%self.size
    
    def get(self,key):
        """Gets data back through key
        Arguments:
            key {Object}
        Returns:
            data {Object}
        """
        startslot = self.hashfunction(key)
        collisions = 0
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                collisions += 1
                position=self.rehash(position,collisions)
                if position == startslot:
                    stop = True
        return data

    def __delitem__(self,key):
        """Overloads dunder del method
        Arguments:
            key {Object} -- key to be deleted
        """
        startslot = self.hashfunction(key)
        stop = False
        collisions = 0
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                self.slots[position] = 'deleted'
                self.data[position]= None
            else:
                collisions += 1
                position=self.rehash(position,collisions)
                if position == startslot:
                    stop = True 

    def __getitem__(self,key):
        """Overrides dunder __getitem__ method to use bracket notation on class
        Arguments:
            key {Object}
        Returns:
            data {Object}
        """
        return self.get(key)

    def __setitem__(self,key,data):
        """Overrides dunder __setitem__ method to use bracket notation on class
        Ex: hastable['apple'] = 'orange'
        Arguments:
            key {Object}
        """
        self.put(key,data)
    
    def __len__(self):
        """Overrides dunder __len__ method to use standard python notation
        Ex: hastable['apple'] = 'orange'
        Returns: number of keys in use
        """
        return len(self.keys())
    
    def keys(self):
        """Returns list of keys
        Returns: {List} - keys
        """
        return list(filter(lambda x: x is not None, self.slots))
    
    def values(self):
        """Returns list of values
        Returns: {List} - values
        """
        return list(filter(lambda x: x is not None, self.data))

    def items(self):
        """Returns tuples of key,value pairs
        Returns: {Tuples} - key,value pairs
        """
        return list((k, v) for k, v in zip(self.slots, self.data)
            if k is not None and v is not None)

def randomString(stringLength=6):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def test_hash():
    """Test function for class methods"""
    hashtable = HashTable()
    keys = [randomString() for _ in range(75)]
    values = [random.randint(0,10) for _ in range(75)]
    items = list((k, v) for k, v in zip(keys, values))
    for key,value in items:
        hashtable.put(key,value)

    keys = hashtable.keys()
    hashtable.put('test',1234)
    del hashtable['test']
    hashtable.put('test',1234)
    for key in keys:
        print(hashtable[key])
