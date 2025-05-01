def big_sum(nums):
    if not nums:  # Check if the list is empty
        return 0
    min_val = max_val = nums[0]  # Initialize min and max with the first element
    for num in nums[1:]:  # Start from the second element
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    sum_of_extremes = min_val + max_val  # Calculate the sum of the smallest and largest values
    return sum_of_extremes