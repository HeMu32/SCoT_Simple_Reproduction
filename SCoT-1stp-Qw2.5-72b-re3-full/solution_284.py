def check_element(lst, element):
    result = True
    for item in lst:
        if item != element:
            result = False
            break
    return result