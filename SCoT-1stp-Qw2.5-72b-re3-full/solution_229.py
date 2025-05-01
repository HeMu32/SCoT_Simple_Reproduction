def re_arrange_array(arr, n):
    negatives = []
    positives = []
    for num in arr:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)
    return negatives + positives