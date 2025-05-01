def common_element(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return bool(set1 & set2)