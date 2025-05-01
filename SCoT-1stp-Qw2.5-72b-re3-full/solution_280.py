def sequential_search(dlist, item):
    index = 0
    for element in dlist:
        if element == item:
            return index
        index += 1
    return -1