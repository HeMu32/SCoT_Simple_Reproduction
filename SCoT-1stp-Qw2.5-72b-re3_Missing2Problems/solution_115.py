def empty_dit(list1):
    all_empty = True
    for d in list1:
        if d:  # If the dictionary is not empty
            all_empty = False
            break
    return all_empty