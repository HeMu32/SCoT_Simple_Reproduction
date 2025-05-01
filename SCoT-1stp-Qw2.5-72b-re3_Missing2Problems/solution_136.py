def cal_electbill(units):
    # Define the rate slabs and their corresponding rates
    slabs = [(100, 0.5), (200, 0.7), (300, 1.0), (float('inf'), 1.5)]
    
    total_bill = 0.0
    
    for i in range(len(slabs)):
        if units <= slabs[i][0]:
            total_bill += units * slabs[i][1]
            break
        else:
            total_bill += (slabs[i][0] if i == 0 else slabs[i][0] - slabs[i-1][0]) * slabs[i][1]
            units -= (slabs[i][0] if i == 0 else slabs[i][0] - slabs[i-1][0])
    
    return total_bill