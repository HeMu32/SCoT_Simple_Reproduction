def get_pell(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  prev1, prev2 = 1, 0
  for _ in range(2, n + 1):
    curr = 2 * prev1 + prev2
    prev2 = prev1
    prev1 = curr
  return prev1