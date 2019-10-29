import random
import time

def time_decorator(fn):
    """Decorator function that when added to function returns execution time
        as well as function return val
    Arguments: fn {function}
    Returns: x (function return val) , time (Execution time)
    """
    def foo(lst,item):
        start = time.time()
        x = fn(lst,item)
        end = time.time()
        return x, end-start
    return foo

def time_decorator_2(fn):
    """Decorator wrapper function that times functions with 3 parameters and one return val
    Arguments: fn {function}
    Returns: x (function return val) , time (Execution time)
    """
    def foo(alist,first,last,item):
        start = time.time()
        x = fn(alist,first,last,item)
        end = time.time()
        return x, end-start
    return foo


def binarySearch(alist, item):
    """Non recursive binary search algo
    Arguments:
        alist {List} 
        item {Object}
    """
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1         
    return found


def rec_bin_search(alist, item):
    """Recursive binary search algo
    Arguments:
        alist {List} 
        item {Object}
    """
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return rec_bin_search(alist[:midpoint],item)
            else:
                return rec_bin_search(alist[midpoint+1:],item)

'''
Exercise # 1
Set up a random experiment to test the difference between a sequential search and a
binary search on a list of integers. Use the binary search functions given in the text
(recursive and iterative). Generate a random, ordered list of integers and do a benchmark
analysis for each one. What are your results? Can you explain them?

Results: The recursive algorithm grows exponentially over time where the non recursive algorithm
stays roughly the same. I belive this is due to the slice operators that are O(n)
'''
def time_test_binary_search():
    """Test recursive binary search function vs non recursive binary search function.
    Must add time decorators to functions before running test
    Returns: {String} -- Time results for 2 algorithms
    """
    lst = [i for i in range(10000000)]
    item = random.randint(0,10000000)
    x,y = rec_bin_search(lst,item)
    a,b = binarySearch(lst,item)
    return f'Recursive Time:{y}, Non Recursive:{b}'


'''
Exercise # 2:
Implement the binary search using recursion without the slice operator. Recall that you
will need to pass the list along with the starting and ending index values for the sublist.
Generate a random, ordered list of integers and do a benchmark analysis.
'''
def recur_bin_srch_noslice(alist,first,last,item):
    """Recursive binary search without the slice
    Arguments: 
        {List} 
        {Integer} - First index in list
        {Integer} - Last index in list
        {Object} - Object to search for
    Returns: {Boolean}
    """
    if last>=first:
        midpoint = (first + last)//2
        if alist[midpoint]==item:
            return True
        else:
            if alist[midpoint] > item:
                return recur_bin_srch_noslice(alist,first,midpoint-1,item)
            else:
                return recur_bin_srch_noslice(alist,midpoint+1,last,item)
    else:
        return False

def time_test_new_binary_search():
    """Test recursive binary search function w/o slice vs non recursive binary search function
    Must add time decorator on rec_bin_search() function and recur_bin_srch_noslice() function
    Returns: {String} -- Time results for 2 algorithms
    """
    lst = [i for i in range(10000000)]
    item = random.randint(0,10000000)
    a,b = rec_bin_search(lst,item)
    x,y = recur_bin_srch_noslice(lst,0,len(lst)-1,item)
    
    return f'Recursive Time:{b}, Recursive Time w/o Slice:{y}'