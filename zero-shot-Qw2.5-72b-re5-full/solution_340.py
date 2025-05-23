def sum_three_smallest_nums(lst):
    """
    Write a python function to find the sum of the three lowest positive numbers from a given list of numbers.
    """
    positive_nums = [num for num in lst if num > 0]
    positive_nums.sort()
    return sum(positive_nums[:3]) if len(positive_nums) >= 3 else None