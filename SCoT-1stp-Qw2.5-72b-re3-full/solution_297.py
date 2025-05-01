def flatten_list(list1):
    flat_list = []

    def flatten(item):
        if isinstance(item, list):
            for element in item:
                flatten(element)
        else:
            flat_list.append(item)

    for item in list1:
        flatten(item)
    
    return flat_list