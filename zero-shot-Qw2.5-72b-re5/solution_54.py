def counting_sort(my_list):
    if not my_list:
        return []

    max_val = max(my_list)
    min_val = min(my_list)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    output = [0] * len(my_list)

    for number in my_list:
        count[number - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for number in reversed(my_list):
        output[count[number - min_val] - 1] = number
        count[number - min_val] -= 1

    return output