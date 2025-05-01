def find_lists(Input):
    count = 0
    for element in Input:
        if isinstance(element, list):
            count += 1
    return count