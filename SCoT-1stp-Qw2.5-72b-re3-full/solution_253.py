def count_integer(list1):
    count = 0
    for element in list1:
        if isinstance(element, int):
            count += 1
    return count