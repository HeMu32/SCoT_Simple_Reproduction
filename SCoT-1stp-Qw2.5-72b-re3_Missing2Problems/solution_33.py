def decimal_To_Binary(N):
    binary_str = ""
    while N > 0:
        remainder = N % 2
        binary_str = str(remainder) + binary_str
        N = N // 2
    if binary_str == "":
        binary_str = "0"
    return binary_str