def index_minimum(test_list):
    min_value = None
    index = -1
    for idx, tup in enumerate(test_list):
        # Assuming the value to compare is the first element of the tuple
        value = tup[0]
        if min_value is None or value < min_value:
            min_value = value
            index = idx
    return index