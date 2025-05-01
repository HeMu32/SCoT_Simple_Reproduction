def frequency_lists(list1):
    frequency_dict = {}
    for sublist in list1:
        # Convert sublist to tuple to use as a dictionary key
        tuple_sublist = tuple(sublist)
        if tuple_sublist in frequency_dict:
            frequency_dict[tuple_sublist] += 1
        else:
            frequency_dict[tuple_sublist] = 1
    return frequency_dict