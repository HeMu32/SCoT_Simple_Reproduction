def sum_negativenum(nums):
    # Filter the list to include only negative numbers
    negative_nums = list(filter(lambda x: x < 0, nums))
    # Calculate the sum of the negative numbers
    sum_neg = sum(negative_nums)
    # Return the sum
    return sum_neg