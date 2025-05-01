def count_odd(array_nums):
    odd_elements = list(filter(lambda x: x % 2 != 0, array_nums))
    return len(odd_elements)