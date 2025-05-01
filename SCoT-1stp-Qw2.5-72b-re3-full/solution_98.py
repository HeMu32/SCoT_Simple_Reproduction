def multiply_num(numbers):
    product = 1
    length = len(numbers)
    
    if length == 0:
        return 0
    else:
        for number in numbers:
            product *= number
        result = product / length
        return result