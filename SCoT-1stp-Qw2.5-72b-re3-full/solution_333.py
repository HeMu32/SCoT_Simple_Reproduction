def Sort(sub_li):
    # Sort the list using the second element of each sublist as the key
    return sorted(sub_li, key=lambda x: x[1])