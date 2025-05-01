def is_majority(arr, n, x):
    count = 0
    for element in arr:
        if element == x:
            count += 1
        if count > n // 2:
            return True
    return False