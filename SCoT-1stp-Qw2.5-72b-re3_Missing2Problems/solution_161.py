def remove_elements(list1, list2):
    result = []
    for element in list1:
        if element not in list2:
            result.append(element)
    return result