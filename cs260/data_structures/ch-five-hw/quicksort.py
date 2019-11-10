import random
import time
import copy

'''
Exercise #14:
One way to improve the quick sort is to use an insertion sort on lists that have a small
length (call it the “partition limit”). Why does this make sense? Re-implement the quick
sort and use it to sort a random list of integers. Perform an analysis using different list
sizes for the partition limit.

Exercise #15:
Implement the median-of-three method for selecting a pivot value as a modification to
quick_sort. Run an experiment to compare the two techniques.
'''
def time_me(fn):
    """Time decorator function used for function with 3 param
    Arguments:
        fn {function} -- [description]
    Returns {Float} - time function took to run
    """
    def callback(alist,first,last):
        start = time.time()
        fn(alist,first,last)
        end = time.time()
        return end-start
    return callback


def quickSort(alist,first,last):
    """Function to sort numbers from small to large
    Arguments:
        alist {List} -- [description]
        first {int} -- first index in alist
        last {int} -- last index in alist
    """
    if first<last:
        pivot = partition(alist,first,last)
        quickSort(alist,first,pivot-1)
        quickSort(alist,pivot+1,last)


def quickSortWithMedian3(alist,first,last):
    """Function to sort numbers from small to large.
    Uses the median of 3 to find pivot
    Arguments:
        alist {List} -- [description]
        first {int} -- first index in alist
        last {int} -- last index in alist
    """
    if first<last:
        pivot = partition_median_3(alist,first,last)
        quickSort(alist,first,pivot-1)
        quickSort(alist,pivot+1,last)
        

def quickSortWithInsertion(alist,first,last):
    """Function to sort numbers from small to large.
    Uses insetion sort for lists smaller than 10
    Arguments:
        alist {List} -- [description]
        first {int} -- first index in alist
        last {int} -- last index in alist
    """
    if first<last:
        if last - first < 10:
           insertionSort(alist,first,last)

        else:
            pivot = partition(alist,first,last)
            quickSort(alist,first,pivot-1)
            quickSort(alist,pivot+1,last)


def median(first, mid, last):
    """Finds median of 3 parameters
    Arguments:
        first {tuple} -- (int,int) -- number,index
        mid {tuple} -- (int,int) -- number,index
        last {tuple} -- (int,int) -- number,index
    Returns:
        median {tuple} -- median of 3 param numbers
    """
    median = last
    if (first[0] - mid[0]) * (last[0] - first[0]) >= 0:
        median = first
    elif (mid[0] - first[0]) * (last[0] - mid[0]) >= 0:
        median = mid
    return median

def partition_median_3(alist,first,last):
    """Finds pivot number by taking median of first last and middle index.
    Mutates list so all numbers smaller than pivot number are to left and larger to right
    Arguments:
        alist {List}
        first {int} -- first index val
        last {int} -- last index val
    Returns: index of pivot point after sorting
    """
    midindex = (last-first) // 2
    pivotvalue,pivotindex = median((alist[first],first), (alist[midindex],midindex), (alist[last],last))
    alist[pivotindex] = alist[first] #puts left val at pivot index
    alist[first] = pivotvalue #puts pivot val at left index
    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def partition(alist,first,last):
    """Takes first number in list as pivot val and mutates list so all numbers smaller 
    than pivot number are to left and larger to right
    Arguments:
        alist {List}
        first {int} -- first index val
        last {int} -- last index val
    Returns: index of pivot point after sorting
    """
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def insertionSort(alist,low,hi):
    """Function to sort numbers from small to large
    Arguments:
        alist {List} -- [description]
        low {int} -- first index in alist
        hi {int} -- last index in alist
    """
    for index in range(low + 1,hi + 1,1):

        currentvalue = alist[index]
        position = index

        while position>low and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue


def quicksort_vs_quick_w_insertion():
    """Test quicksort time vs quicksort with insertion sort time
    Must add time decorator @time_me to functions quickSort() and quickSortWithInsertion()
    Returns: {String} -- Time results for 2 algorithms
    """
    alist  = [random.randint(0,100) for _ in range(100)]
    alist2 = copy.deepcopy(alist)
    qs_time = quickSort(alist,0,len(alist)-1)
    qs_optimized_time = quickSortWithInsertion(alist2,0,len(alist)-1)
    return f'Quicksort Time:{qs_time}\nQuicksort with Insertion Sort Time:{qs_optimized_time}'

def quicksort_vs_quick_w_median_3():
    """Test quicksort time vs quicksort with insertion sort time
    Must add time decorator @time_me to functions quickSort() and quickSortWithMedian3()
    Returns: {String} -- Time results for 2 algorithms
    """
    alist  = [random.randint(0,100) for _ in range(10000)]
    alist2 = copy.deepcopy(alist)
    qs_time = quickSort(alist,0,len(alist)-1)
    qs_optimized_time = quickSortWithMedian3(alist2,0,len(alist)-1)
    return f'Quicksort Time:{qs_time}\nQuicksort with Median 3 Time:{qs_optimized_time}'

#print(quicksort_vs_quick_w_insertion())
