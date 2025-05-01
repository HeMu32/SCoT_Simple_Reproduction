def remove_replica(test_tup):
    res = []
    count_dict = {}
    
    # Count occurrences of each element
    for element in test_tup:
        if element not in count_dict:
            count_dict[element] = 1
        else:
            count_dict[element] += 1
    
    # Replace duplicates with 'custom_value'
    for element in test_tup:
        if count_dict[element] == 1:
            res.append(element)
        else:
            res.append('custom_value')
    
    return tuple(res)