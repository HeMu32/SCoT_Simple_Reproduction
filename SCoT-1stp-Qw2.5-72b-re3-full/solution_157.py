def encode_list(list1):
    encoded_list = []
    current_group = []
    current_element = None
    
    for element in list1:
        if element == current_element:
            current_group.append(element)
        else:
            if current_group:
                encoded_list.append((len(current_group), current_element))
                current_group = []
            current_element = element
            current_group.append(element)
    
    if current_group:
        encoded_list.append((len(current_group), current_element))
    
    return encoded_list