def frequency_lists(list1):
    from collections import Counter
    flattened_list = [item for sublist in list1 for item in sublist]
    frequency_count = Counter(flattened_list)
    return frequency_count