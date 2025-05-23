def remove_replica(test_tup):
    from collections import Counter
    count = Counter(test_tup)
    result = tuple(item if count[item] == 1 else 'custom_value' for item in test_tup)
    return result