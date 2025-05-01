def convert_list_dictionary(l1, l2, l3): 
    return {key: {l2[i]: l3[i] for i in range(len(l2))} for key in l1}