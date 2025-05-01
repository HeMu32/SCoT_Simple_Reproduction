def replace_char(str1, ch, newch):
    result = ""
    for c in str1:
        if c == ch:
            result += newch
        else:
            result += c
    return result