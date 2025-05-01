def add_consecutive_nums(nums):
    result = []
    for i in range(len(nums) - 1):
        result.append(nums[i] + nums[i + 1])
    return result