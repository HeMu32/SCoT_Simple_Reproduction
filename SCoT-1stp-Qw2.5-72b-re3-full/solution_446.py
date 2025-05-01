def count_Occurrence(tup, lst):
    count_dict = {}
    for ele in lst:
        count = 0
        for item in tup:
            if item == ele:
                count += 1
        count_dict[ele] = count
    return count_dict