import heapq

def heap_replace(heap, a):
    """
    Write a function to delete the smallest element from the given heap and then insert a new item.
    """
    heapq.heapreplace(heap, a)