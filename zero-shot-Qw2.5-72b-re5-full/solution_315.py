def find_Max_Len_Even(str): 
    words = str.split()
    max_len = 0
    for word in words:
        if len(word) % 2 == 0 and len(word) > max_len:
            max_len = len(word)
    return max_len