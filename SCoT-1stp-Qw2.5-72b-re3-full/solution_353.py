def remove_column(list1, n):
    result = []
    for sublist in list1:
        new_sublist = []
        for i in range(len(sublist)):
            if i != n:
                new_sublist.append(sublist[i])
        result.append(new_sublist)
    return result