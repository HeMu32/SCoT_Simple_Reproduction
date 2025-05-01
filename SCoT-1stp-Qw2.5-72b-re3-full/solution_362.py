def max_occurrences(nums):
    count_dict = {}
    for item in nums:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    max_item = None
    max_count = 0
    for item, count in count_dict.items():
        if count > max_count:
            max_item = item
            max_count = count
    
    return max_item