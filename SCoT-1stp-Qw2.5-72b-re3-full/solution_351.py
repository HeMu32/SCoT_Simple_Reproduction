def first_Element(arr, n, k):
    count_dict = {}
    for i in range(n):
        if arr[i] in count_dict:
            count_dict[arr[i]] += 1
        else:
            count_dict[arr[i]] = 1
    
    for i in range(n):
        if count_dict[arr[i]] == k:
            return arr[i]
    
    return -1