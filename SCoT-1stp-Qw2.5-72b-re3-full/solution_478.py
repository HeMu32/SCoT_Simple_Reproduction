def remove_lowercase(str1):
    result = ""
    for ch in str1:
        if not ch.islower():
            result += ch
    return result