def multi_list(rownum, colnum):
    # Initialize the result list
    result = []
    
    # Loop for each row
    for i in range(rownum):
        # Initialize the current row
        row = []
        
        # Loop for each column in the current row
        for j in range(colnum):
            # Append a default value (0) to the current row
            row.append(0)
        
        # Append the current row to the result list
        result.append(row)
    
    # Return the two-dimensional array
    return result