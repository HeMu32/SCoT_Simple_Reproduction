def all_unique(test_list):
    seen = set()
    for element in test_list:
        if element in seen:
            return False
        seen.add(element)
    return True