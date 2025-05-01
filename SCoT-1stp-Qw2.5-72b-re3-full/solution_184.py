def greater_specificnum(list, num):
    result = []
    for element in list:
        if element > num:
            result.append(element)
    return result