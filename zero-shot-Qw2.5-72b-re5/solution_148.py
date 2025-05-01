def sum_digits_single(n): 
    """ 
    Write a function to divide a number into two parts such that the sum of digits is maximum. 
    """ 
    def sum_of_digits(x):
        return sum(int(digit) for digit in str(x))
    
    max_sum = 0
    best_split = (0, 0)
    
    for i in range(1, n):
        part1 = i
        part2 = n - i
        current_sum = sum_of_digits(part1) + sum_of_digits(part2)
        if current_sum > max_sum:
            max_sum = current_sum
            best_split = (part1, part2)
    
    return best_split