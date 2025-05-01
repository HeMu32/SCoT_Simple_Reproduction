def position_max(list1):
    if not list1:
        return []
    max_val = max(list1)
    return [index for index, value in enumerate(list1) if value == max_val]