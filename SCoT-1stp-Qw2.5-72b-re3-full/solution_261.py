def division_elements(test_tup1, test_tup2):
    result_list = []
    for num1, num2 in zip(test_tup1, test_tup2):
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        else:
            result = num1 / num2
            result_list.append(result)
    result_tup = tuple(result_list)
    return result_tup