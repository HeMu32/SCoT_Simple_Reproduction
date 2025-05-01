def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = str(n % 2)
        binary = remainder + binary
        n = n // 2
    if binary == "":
        binary = "0"
    return binary