def frequency_Of_Largest(n, arr):
    if n == 0:
        return 0
    max_value = max(arr)
    return arr.count(max_value)