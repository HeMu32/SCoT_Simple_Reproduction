def positive_count(nums):
    positive_count = 0
    total_count = len(nums)
    
    for num in nums:
        if num > 0:
            positive_count += 1
    
    ratio = positive_count / total_count
    return ratio