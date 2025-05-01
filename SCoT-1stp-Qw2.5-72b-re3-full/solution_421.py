def concatenate_tuple(test_tup, delimiter=' '):
    result = ''
    for element in test_tup:
        element_str = str(element)
        if result == '':
            result += element_str
        else:
            result += delimiter + element_str
    return result