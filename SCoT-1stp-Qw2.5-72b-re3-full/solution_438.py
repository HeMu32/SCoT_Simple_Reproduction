def count_bidirectional(test_list):
    count = 0
    for i, pair in enumerate(test_list):
        for j in range(i + 1, len(test_list)):
            if pair == test_list[j][::-1]:
                count += 1
    return count