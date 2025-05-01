def average_Odd(N):
    sum_of_odds = 0
    count_of_odds = 0
    for i in range(1, N + 1):
        if i % 2 != 0:
            sum_of_odds += i
            count_of_odds += 1
    avg = sum_of_odds / count_of_odds
    return avg