def round_and_sum(list1):
    total_sum = 0
    for number in list1:
        rounded_number = round(number)
        total_sum += rounded_number
    result = total_sum * len(list1)
    print(result)