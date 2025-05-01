def tuple_intersection(test_list1, test_list2):
    intersection = []
    for t1 in test_list1:
        for t2 in test_list2:
            if sorted(t1) == sorted(t2):
                intersection.append(t1)
                break  # Avoid adding duplicates
    return intersection