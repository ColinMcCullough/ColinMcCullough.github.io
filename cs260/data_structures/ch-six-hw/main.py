"""
    Binheap Runner
"""
from random import randint
from binheap import BinHeap

def random_list(low=0, high=100, count=20):
    return [randint(low, high) for _ in range(count)]


def main():
    #nums = random_list(count=11)
    nums = [11, 46, 78, 64, 17, 74, 95, 16, 28, 6,75]
    print("List:", nums)
    heap = BinHeap()
    heap.build_heap(nums)
    heap.insert(5)
    print("List:", heap.heapList)
    #print("Heap:", heap.heapList)
    #heap.sort()
    #print("Sorted:", heap.heapList)

main()