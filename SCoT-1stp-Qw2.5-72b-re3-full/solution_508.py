def same_order(l1, l2):
    common = []
    for e in l1:
        if e in l2 and e not in common:
            common.append(e)
    
    index = 0
    for e in l2:
        if e in common:
            if e == common[index]:
                index += 1
            else:
                return False
    
    return index == len(common)