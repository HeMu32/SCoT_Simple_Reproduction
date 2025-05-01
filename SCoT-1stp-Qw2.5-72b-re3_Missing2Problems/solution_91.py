def find_substring(str1, sub_str):
    result = False
    for i in range(len(str1) - len(sub_str) + 1):
        if str1[i:i+len(sub_str)] == sub_str:
            result = True
            break
    return result