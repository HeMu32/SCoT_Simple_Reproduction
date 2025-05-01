def index_on_inner_list(list_data, index_no):
    # Sort the list of lists based on the specified index of the inner lists
    sorted_list = sorted(list_data, key=lambda x: x[index_no])
    return sorted_list