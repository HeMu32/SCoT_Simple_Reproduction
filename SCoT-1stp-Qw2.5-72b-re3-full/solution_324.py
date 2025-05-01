def sum_of_alternates(test_tuple):
    sum_of_alternates = 0
    for index, element in enumerate(test_tuple):
        if index % 2 == 0:  # Check if the index is even
            sum_of_alternates += element
    return sum_of_alternates