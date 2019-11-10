import random
from timeit import Timer
import time

#Question 1: Devise an expirement to verify that the list index operator is O(1)
def list_index_time(srt,mx,stp):
    """Test the time it takes to access items in a list as it grows
    Returns: {Dictionary} - (key(range),value(time to access))
    """
    test_result = {}
    for number in range(srt,mx,stp):
        rndnum = random.randint(0,number)
        lst = list(range(number))
        test_result[number] = get_indx_time(lst,rndnum)
    return test_result

def get_indx_time(lst,index):
    """Test time it takes to access items by key in a list  as it grows
    Return: {Float} 
    """
    if index >= len(lst):
        raise IndexError('Index out of bounds')
    else:
        strt = time.time()
        for repeat in range(1000):
            x = lst[index]
        stop = time.time()
        return stop-strt

#Question 2: Devise an expirement to verify that the get item and set item are O(1) in dictionaries
def dictionary_get_time(srt,mx,stp):
    """Test time it takes to access items by key in a  dictionary as it grows
    Return: {dictionary} (key(range),value(time to access))
    """
    test_result = {} 
    for number in range(srt,mx,stp):
        rndnum = random.randint(0,number)
        dictionary = {j:None for j in range(number)}
        test_result[number] = get_indx_time(dictionary,rndnum)
    return test_result

def dictionary_set_time(srt,mx,stp):
    """Test time it takes to change values by key in a dictionary as it grows in size
    Return: {dictionary} (key(range),value(time to mutate))
    """
    test_result = {}
    for number in range(srt,mx,stp):
        rndnum = random.randint(0,number)
        dictionary = {j:None for j in range(number)}
        test_result[number] = get_set_dict_time(dictionary,rndnum)
    return test_result

def get_set_dict_time(dict,key):
    """Times updating values in dictionary
    Arguments:
        dict {dictionary}
        key {int}
    """
    strt = time.time()
    for repeat in range(1000):
        dict[key] = 'test'
    stop = time.time()
    return stop-strt

#Question 3: Devise an expirement that compares the performance of del in list and dictionary
def lst_vs_dictionary_del_time(srt,mx,stp):
    """Compares delete function run time on dictionary and list as they grow in size
    Return {List,Dictionary} - Key in dictionary is size of Dictiononary, Value is Time to delete
    """
    lst_times = []
    dictionary_times = {}
    for number in range(srt,mx,stp):
        current_lst = list(range(number))
        current_dct = {j:None for j in range(number)}
        lst_times.append(del_lst_time(current_lst))
        dictionary_times[number] = del_dict_time(current_dct)
    return lst_times, dictionary_times
    
def del_lst_time(lst):
    """ Deleted 1st element in a list
    Arguments: lst {List}
    Return: {Float}
    """
    repeat_times = 10000
    if len(lst) < repeat_times:
        repeat_times = len(lst)
    strt = time.time()
    for repeat in range(repeat_times):
        del lst[0]
    stop = time.time()
    return stop-strt

def del_dict_time(dct):
    """ Times how long it takes to delete item in dictionary
    Arguments: lst {Dictionary}
    Return: {Float}
    """
    repeat_times = 10000
    if len(dct) < repeat_times:
        repeat_times = len(dct)
    strt = time.time()
    for num in range(repeat_times):
        del dct[num]
    stop = time.time()
    return stop-strt


#Question 4: Given a list of numbers in random order, write a O nlog(n) algo that finds the k smallest
#            element in the list 
def find_k_smallest_n_log_n(k,lst):
    """ Finds the k smallest number in a list at O nlog(n) 
    Arguments: k {int}, lst {List}
    Return: {int}
    """
    if not isinstance(k,int) or not isinstance(lst,list):
        raise TypeError('parameters are not correct types')
    if len(lst) < 1:
        raise Exception('list cannot be empty')
    if k > len(lst) - 1:
        raise Exception('k is greater than the list length')
    lst.sort()
    return lst[k-1]

def gen_rndm_num_arr(length):
    """Generates list of random numbers in the range of the length specified in the param
    Arguments: length {int}
    Return: {List}
    """
    return [random.randint(0,length - 1) for _ in range(length)]