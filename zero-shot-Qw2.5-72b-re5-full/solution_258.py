def count_odd(array_nums):
    return len(list(filter(lambda x: x % 2 != 0, array_nums)))