def check_k_elements(test_list, K):
    all_have_k_elements = True
    for t in test_list:
        if len(t) != K:
            all_have_k_elements = False
            break
    return all_have_k_elements