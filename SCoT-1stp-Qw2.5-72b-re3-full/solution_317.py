def modified_encode(alist):
    encoded_list = []
    if not alist:
        return encoded_list

    current_element = alist[0]
    count = 1

    for element in alist[1:]:
        if element == current_element:
            count += 1
        else:
            if count > 1:
                encoded_list.append((count, current_element))
            else:
                encoded_list.append(current_element)
            current_element = element
            count = 1

    if count > 1:
        encoded_list.append((count, current_element))
    else:
        encoded_list.append(current_element)

    return encoded_list