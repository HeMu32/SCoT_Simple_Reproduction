def find_remainder(arr, lens, n):
    product = 1
    for i in range(lens):
        product = (product * (arr[i] % n)) % n
    return product