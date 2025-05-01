def decimal_to_Octal(deciNum):
    octal = ""
    while deciNum > 0:
        remainder = deciNum % 8
        octal = str(remainder) + octal
        deciNum = deciNum // 8
    if octal == "":
        octal = "0"
    return octal