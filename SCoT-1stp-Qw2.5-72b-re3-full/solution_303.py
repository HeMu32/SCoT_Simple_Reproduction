def solve(a, n):
    count1 = 0
    count2 = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                count1 += 1
            if a[i] < a[j]:
                count2 += 1
    
    return count1 == count2