def get_Char(strr): 
    total = 0
    for char in strr:
        total += ord(char)
    return chr(total % 256)