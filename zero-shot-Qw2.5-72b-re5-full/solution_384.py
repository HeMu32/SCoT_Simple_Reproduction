def frequency_Of_Smallest(n, arr):
    if n == 0:
        return 0
    smallest = min(arr)
    frequency = arr.count(smallest)
    return frequency