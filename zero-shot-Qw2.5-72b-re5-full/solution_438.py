def count_bidirectional(test_list):
    """
    Write a function to count bidirectional tuple pairs.
    """
    count_dict = {}
    for (x, y) in test_list:
        if (x, y) in count_dict:
            count_dict[(x, y)] += 1
        elif (y, x) in count_dict:
            count_dict[(y, x)] += 1
        else:
            count_dict[(x, y)] = 1
    return count_dict