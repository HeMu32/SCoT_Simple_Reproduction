import heapq

def heap_queue_smallest(nums, n):
    """
    Write a function to find the smallest integers from a given list of numbers using heap queue algorithm.
    """
    return heapq.nsmallest(n, nums)