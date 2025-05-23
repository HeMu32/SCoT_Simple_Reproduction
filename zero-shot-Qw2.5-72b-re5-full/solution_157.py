def encode_list(list1):
    if not list1:
        return []
    
    encoded_list = []
    current = list1[0]
    count = 1
    
    for item in list1[1:]:
        if item == current:
            count += 1
        else:
            encoded_list.append((current, count))
            current = item
            count = 1
    encoded_list.append((current, count))
    
    return encoded_list