def check_triplet(A, n, target_sum, count):
    A.sort()
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = A[i] + A[left] + A[right]
            if current_sum == target_sum:
                count[0] += 1
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return count[0] > 0