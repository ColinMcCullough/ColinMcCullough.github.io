class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
'''
s=Stack()
#Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
def revstring(string):
    s=Stack()
    revstr = ''
    for letter in string:
        s.push(letter)
    while not s.isEmpty():
        revstr += s.pop()
    return revstr

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

def decimal_to_binary(number):
    bin_str = ""
    s = Stack()
    while number > 0:
        remain = number % 2
        number = number // 2
        s.push(remain)
    while not s.isEmpty():
        bin_str += str(s.pop())
    return bin_str

def base_converter(number,base):
    digits = "0123456789ABCDEF"
    base_str = ""
    s = Stack()
    while number > 0:
        remain = number % base
        s.push(remain)
        number = number // base    
    while not s.isEmpty():
        base_str += digits[s.pop()]
    return base_str
'''


