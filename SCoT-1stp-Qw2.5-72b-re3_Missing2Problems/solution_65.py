def recursive_list_sum(data_list):
    total_sum = 0
    for element in data_list:
        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, list):
            total_sum += recursive_list_sum(element)
    return total_sum