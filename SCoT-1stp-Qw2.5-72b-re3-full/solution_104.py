def sort_sublists(input_list):
    # Using list comprehension and sorted with a lambda function to sort each sublist
    sorted_list = [sorted(sublist, key=lambda x: x) for sublist in input_list]
    return sorted_list