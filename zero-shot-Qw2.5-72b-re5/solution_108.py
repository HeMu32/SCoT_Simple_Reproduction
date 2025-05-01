import heapq

def merge_sorted_list(num1, num2, num3):
    """
    Write a function to merge multiple sorted inputs into a single sorted iterator using heap queue algorithm.
    """
    return heapq.merge(num1, num2, num3)