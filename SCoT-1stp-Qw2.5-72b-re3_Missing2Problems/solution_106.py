def add_lists(test_list, test_tup):
    res = []
    min_length = min(len(test_list), len(test_tup))
    
    for i in range(min_length):
        res.append(test_list[i] + test_tup[i])
    
    if len(test_list) > len(test_tup):
        res.extend(test_list[min_length:])
    elif len(test_tup) > len(test_list):
        res.extend(list(test_tup[min_length:]))
    
    return res