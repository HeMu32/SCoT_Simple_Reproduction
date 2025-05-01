def check_value(dict, n):
    result = True
    for value in dict.values():
        if value != n:
            result = False
            break
    return result