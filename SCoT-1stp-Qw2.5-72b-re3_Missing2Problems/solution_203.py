def hamming_Distance(x, y):
    # Convert integers to binary and remove the '0b' prefix
    bin_x = bin(x)[2:]
    bin_y = bin(y)[2:]
    
    # Pad the shorter binary string with leading zeros
    max_len = max(len(bin_x), len(bin_y))
    bin_x = bin_x.zfill(max_len)
    bin_y = bin_y.zfill(max_len)
    
    # Initialize the Hamming distance
    distance = 0
    
    # Calculate the Hamming distance
    for i in range(max_len):
        if bin_x[i] != bin_y[i]:
            distance += 1
    
    return distance