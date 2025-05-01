def max_difference(test_list):
    max_diff = 0
    for a, b in test_list:
        diff = abs(a - b)
        if diff > max_diff:
            max_diff = diff
    return max_diff