def len_log(list1):
    max_length = 0
    for word in list1:
        if len(word) > max_length:
            max_length = len(word)
    return max_length