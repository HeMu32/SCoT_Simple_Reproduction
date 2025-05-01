def rear_extract(test_list):
    result = []
    for tup in test_list:
        result.append(tup[-1])
    return result