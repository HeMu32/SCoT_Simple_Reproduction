def decode_list(alist):
    """ 
    Write a function to decode a run-length encoded given list. 
    """ 
    decoded_list = []
    for item in alist:
        if isinstance(item, int):
            count = item
        else:
            decoded_list.extend([item] * count)
    return decoded_list