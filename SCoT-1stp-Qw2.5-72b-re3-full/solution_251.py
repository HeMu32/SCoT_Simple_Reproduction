def insert_element(lst, element):
    new_list = []
    for item in lst:
        new_list.append(element)
        new_list.append(item)
    return new_list