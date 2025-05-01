def remove_even(str1):
    result = ""
    for i in range(len(str1)):
        if i % 2 == 1:
            result += str1[i]
    return result