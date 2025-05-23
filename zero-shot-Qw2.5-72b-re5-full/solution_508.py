def same_order(l1, l2):
    common_elements = set(l1) & set(l2)
    l1_filtered = [x for x in l1 if x in common_elements]
    l2_filtered = [x for x in l2 if x in common_elements]
    return l1_filtered == l2_filtered