def decimal_to_Octal(deciNum): 
    octalNum = ""
    while deciNum > 0:
        octalNum = str(deciNum % 8) + octalNum
        deciNum = deciNum // 8
    return octalNum if octalNum else "0"