def get_total_number_of_sequences(m, n):
    count = 0
    
    def count_sequences(index, prev, m):
        nonlocal count
        if index == n:
            count += 1
            return
        for i in range(max(1, 2 * prev), m + 1):
            count_sequences(index + 1, i, m)
    
    count_sequences(0, 0, m)
    return count