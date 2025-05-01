def sum_of_digits(nums):
    result = []
    for num in nums:
        num_str = str(num)
        digit_sum = 0
        for char in num_str:
            digit_sum += int(char)
        result.append(digit_sum)
    return result