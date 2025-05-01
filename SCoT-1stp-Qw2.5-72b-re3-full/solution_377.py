def remove_Char(s, char):
    result = ""
    for c in s:
        if c != char:
            result += c
    return result