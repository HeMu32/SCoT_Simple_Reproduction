def get_Char(strr):
    total = 0
    for c in strr:
        total += ord(c)
    result_char = chr(total)
    return result_char