def check_greater(arr, number):
    result = True
    for element in arr:
        if element >= number:
            result = False
            break
    return result