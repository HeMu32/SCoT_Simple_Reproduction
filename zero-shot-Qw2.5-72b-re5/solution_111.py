def common_in_nested_lists(nestedlist):
    from collections import Counter
    flattened_list = [item for sublist in nestedlist for item in sublist]
    item_counts = Counter(flattened_list)
    common_elements = [item for item, count in item_counts.items() if count > 1]
    return common_elements