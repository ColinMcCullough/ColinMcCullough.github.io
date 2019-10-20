import turtle
import random
from timeit import Timer
import time
#Exercise 1
def get_factorial(num):
    """Recursive function to compute the factorial of a number.
    Arguments:
        num {Integer}
    """
    if num < 0:
        raise ValueError('Factorials dont exist for negative numbers')
    if num == 1 or num == 0:
        return 1
    else:
        return num * get_factorial(num - 1)

#Exercise 2
def reverse_lst(lst):
    """Recursive function to reverse a list
    Arguments:
        lst {List}
    """
    if len(lst) <= 1:
        return lst
    else: 
        return lst[-1:] + reverse_lst(lst[:-1])

#Exercise 3
def tree(branchLen,t,size):
    """Recursive function to build tree
    Arguments:
        branchLen {Integer} -- length of branch
        t {Turtle} -- Python turtle module
        size {Integer} -- width of branch
    """
    t.color("green") if branchLen <= 10 else t.color("brown")       
    if branchLen > 5:
        degree,mod = mod_tree_attr(t,size,branchLen)
        t.right(degree)
        tree(branchLen-mod,t,size-1)
        t.left(degree * 2)
        tree(branchLen-mod,t,size-1)
        t.right(degree)
        if branchLen > 15:
            t.color("brown")
        t.backward(branchLen)
     

def mod_tree_attr(t,size,branchLen):
    """Mutates tree attributes
    Arguments:
        t {Turtle} -- Python turtle module
        size {Integer} -- width of branch
        branchLen {Integer} -- length of branch
    Returns
        degree {Integer} - degree the branch will turn
        mod {Integer} - how much shorter branch will be 
    """
    t.pensize(size)
    t.forward(branchLen)
    degree = random.randint(15,40)
    mod = random.randint(6,20)
    return degree,mod

def tree_setup(t):
    """Sets up initial tree attributes 
    Arguments:
        t {Turtle} -- Python turtle module
    """
    t.left(90)
    t.pensize(10) 
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")

def buildtree():
    """Builds a tree with pythons turtle graphics"""
    t = turtle.Turtle()
    myWin = turtle.Screen()
    tree_setup(t)
    tree(100,t,10)
    myWin.exitonclick()

#Exercise 5
def fib(n):
    """Gets the n fibanacci number recursively
    Arguments:
        n {Integer}
    Returns
        {Integer}
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_non_recurse(n):
    """Gets the n fibanacci number non recursively
    Arguments:
        n {Integer}
    Returns
        {Integer}
    """
    a, b, f = 1, 1, 1
    for i in range(2, n):
        f = a + b
        a , b = b, f
    return f

def time_test_fib(n):
    """Test recursive fibanacci function vs non recursive fib function
    Arguments:
        n {Integer} -- [description]
    Returns:
        {String} -- Time results for 2 algorithms
    """
    strt = time.time()
    fib(n)
    stop = time.time()
    recursive_time = stop - strt
    strt = time.time()
    fib_non_recurse(n)
    stop = time.time()
    non_recursive_time = stop - strt
    return f'Recursive Time:{recursive_time}, Non Recursive:{non_recursive_time}'

#Exercise 9,10
'''
Write a program to solve the following problem: You have two jugs: a 4-gallon jug and a 3-gallon jug. 
Neither of the jugs have markings on them. There is a pump that can be used to fill the jugs with water. 
How can you get exactly two gallons of water in the 4-gallon jug? Generalize it for any size
'''
def jug_juggling(bjsize,bjamount,sjsize,sjamount,finalamnt):
    if bjamount == finalamnt: 
        print(f'JugOne:{bjamount}, JugTwo:{sjamount}')
        return True
    else:
        if bjamount == 0 and sjamount == 0:
           return jug_juggling(bjsize,bjsize,sjsize,0,finalamnt)
        if sjamount == 0 and bjamount == bjsize:
            return jug_juggling(bjsize,bjamount-sjsize,sjsize,sjamount+sjsize,finalamnt)
        if sjsize == sjamount:
            return jug_juggling(bjsize,bjsize,sjsize,bjamount,finalamnt)
        if bjamount > 0 and sjamount > 0:
            return jug_juggling(bjsize,bjsize-(sjsize-sjamount),sjsize,sjsize,finalamnt)
        return False