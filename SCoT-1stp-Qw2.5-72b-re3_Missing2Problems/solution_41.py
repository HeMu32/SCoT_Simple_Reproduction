def filter_evennumbers(nums):
    filtered_nums = list(filter(lambda x: x % 2 == 0, nums))
    return filtered_nums