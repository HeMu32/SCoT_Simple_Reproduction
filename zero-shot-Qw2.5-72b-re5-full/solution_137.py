def zero_count(nums):
    """
    Write a function to find the ratio of zeroes in an array of integers.
    """
    zero_count = nums.count(0)
    total_count = len(nums)
    return zero_count / total_count if total_count != 0 else 0