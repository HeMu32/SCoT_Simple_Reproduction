def check_value(dict, n): 
    if len(set(dict.values())) == 1 and list(dict.values())[0] == n:
        return True
    return False