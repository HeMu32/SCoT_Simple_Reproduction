def get_Odd_Occurrence(arr, arr_size):
    result = 0
    for num in arr:
        result ^= num
    return result