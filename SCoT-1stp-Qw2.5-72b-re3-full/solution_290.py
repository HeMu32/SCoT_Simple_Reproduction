def max_length(list1):
    max_len = 0
    max_lists = []
    for sublist in list1:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_lists = [sublist]
        elif len(sublist) == max_len:
            max_lists.append(sublist)
    return max_lists