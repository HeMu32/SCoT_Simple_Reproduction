def convert_list_dictionary(l1, l2, l3):
    nested_dict = {}
    for i in range(len(l1)):
        if l1[i] not in nested_dict:
            nested_dict[l1[i]] = {}
        nested_dict[l1[i]][l2[i]] = l3[i]
    return nested_dict