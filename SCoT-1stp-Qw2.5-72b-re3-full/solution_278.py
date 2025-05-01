def count_first_elements(test_tup):
    result = {}
    count = 0
    for element in test_tup:
        if element not in result:
            result[element] = count
        count += 1
    return result