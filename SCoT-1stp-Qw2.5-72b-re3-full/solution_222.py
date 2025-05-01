def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    first_type = type(test_tuple[0])
    for element in test_tuple:
        if type(element) != first_type:
            return False
    return True