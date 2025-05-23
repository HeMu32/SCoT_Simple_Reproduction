def group_tuples(Input):
    from collections import defaultdict
    
    grouped = defaultdict(list)
    for first, second in Input:
        grouped[first].append(second)
    
    return dict(grouped)