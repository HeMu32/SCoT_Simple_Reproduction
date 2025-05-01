def odd_Days(N): 
    # Function to calculate the number of odd days in a given year
    if N % 400 == 0:
        return 2
    elif N % 100 == 0:
        return 5
    elif N % 4 == 0:
        return 1
    else:
        return 0