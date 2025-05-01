def filter_oddnumbers(nums):
    result = filter(lambda x: x % 2 != 0, nums)
    return list(result)