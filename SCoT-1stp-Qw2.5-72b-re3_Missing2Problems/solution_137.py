def zero_count(nums):
    zero_count = 0
    total_count = len(nums)
    for num in nums:
        if num == 0:
            zero_count += 1
    ratio = zero_count / total_count
    return ratio