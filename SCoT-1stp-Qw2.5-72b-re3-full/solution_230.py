def replace_blank(str1, char):
    new_str = ""
    for c in str1:
        if c == ' ':
            new_str += char
        else:
            new_str += c
    return new_str