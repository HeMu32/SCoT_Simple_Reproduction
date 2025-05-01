def big_sum(nums): 
    """ 
    Write a python function to find the sum of the largest and smallest value in a given array. 
    """ 
    if not nums:
        return 0
    smallest = min(nums)
    largest = max(nums)
    return smallest + largest