def remove_empty(list1):
    result = []
    for sublist in list1:
        if len(sublist) > 0:
            result.append(sublist)
    return result