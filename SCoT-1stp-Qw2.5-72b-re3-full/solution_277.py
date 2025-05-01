def dict_filter(dict, n):
    filtered_dict = {key: value for key, value in dict.items() if value >= n}
    return filtered_dict