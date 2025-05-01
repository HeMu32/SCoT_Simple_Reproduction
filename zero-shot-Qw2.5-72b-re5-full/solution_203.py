def hamming_distance(x, y):
    """
    Write a python function to find the hamming distance between given two integers.
    """
    xor_result = x ^ y
    distance = 0
    while xor_result:
        distance += 1
        xor_result &= xor_result - 1
    return distance