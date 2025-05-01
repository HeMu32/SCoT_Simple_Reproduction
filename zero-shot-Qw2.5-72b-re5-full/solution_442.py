def positive_count(nums):
    """
    Write a function to find the ratio of positive numbers in an array of integers.
    """
    if not nums:
        return 0.0
    
    positive_nums = [num for num in nums if num > 0]
    return len(positive_nums) / len(nums)