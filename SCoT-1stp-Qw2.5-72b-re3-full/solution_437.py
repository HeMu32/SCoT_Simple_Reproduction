def remove_odd(str1):
    result = ""
    for i in range(len(str1)):
        if i % 2 == 0:
            result += str1[i]
    return result